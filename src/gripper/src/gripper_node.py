#!/usr/bin/env python3
import rospy
import numpy as np
import pandas as pd
from simple_pid import PID

from std_msgs.msg import Bool
from ucd_robot.msg import SystemState
from MX28_node import MX28_Controller
from gripper.msg import TargetDelta, TargetForce
from papillarray_ros_v2.msg import SensorState
 
# Constants
DELTA_LIMIT = 82 # Estimated maximum movement per MX28 loop
OUTPUT_INTERVAL = 0.01 # Min. time between new target forces
OPEN_LIMIT = -28000
CLOSE_LIMIT = 28000
MAX_FORCE = 20 #TODO: move_enable is a disaster if still in explore mode 
CRITICAL_FORCE = MAX_FORCE + 5
FORCE_ACCURACY = 0.01 # Accepted force accuracy: +/- 0.05N
POSITION_ACCURACY = 2
WRITE_FREQUENCY = 0.02

MAX_SERVO_TORQUE = 1023
SERVO_RESOLUTION = 1
PRINT_LOG = 1
COM_PORT= "/dev/ttyUSB0"
SERVO_ID = 1


GRIPPER_RATE = 1000

class Gripper_exp1():

    def __init__(self):
        self.node_string = 'Gripper'
        rospy.init_node('Gripper', anonymous=True)
        rospy.loginfo('[%10s] Starting %s'%( self.node_string, self.__class__.__name__))

        # Initialisers
        self.controller = MX28_Controller(port_num=COM_PORT, servo_id=SERVO_ID,resolution=SERVO_RESOLUTION,
                                             torque=MAX_SERVO_TORQUE,print_log=PRINT_LOG)

        # Initiate system variables
        self.torque_enabled = False
        self.system_state = False
        self.move_state = False
        
        # Initiate gripper position variables
        self.target_delta = 0
        self.target_force = 0
        self.current_position = 0
        self.target_position = 0
        self.prev_target_position = 0
        self.prev_target_time = 0

        # Initiate publishers
        self.pub_gripper_state = rospy.Publisher('gripper_state',Bool,queue_size=1)

        # Initiate subscribers
        self.sub_shutdown = rospy.Subscriber('shutdown',Bool,self.shutdown)
        self.sub_system_state = rospy.Subscriber('system_state',SystemState,self.read_system_state)
        self.sub_target_force = rospy.Subscriber('target_force',TargetForce,self.read_target_force)
        self.sub_sensor_state = rospy.Subscriber('/hub_0/sensor_0',SensorState,self.read_sensor)
        self.sub_target_delta = rospy.Subscriber('target_delta',TargetDelta,self.read_target_delta)
        self.sub_gripper_move_state = rospy.Subscriber('gripper_move_state',Bool,self.read_move_state)

        # Read current position
        read_success = False
        while ( not read_success ):
            position = self.controller.MX28_pos()
            if ( type(position) != None ):
                self.initial_position = position
                read_success = True

        self.enable_torque()
        self.rate = rospy.Rate(GRIPPER_RATE)
        self.rosrun()

    def read_system_state(self,msg:SystemState):
        if ( msg.system_state ) and ( not self.system_state ):
            rospy.loginfo('[%10s] System State: True'%self.node_string)
            self.move_state = True
            self.system_state = True

        elif ( not msg.system_state ) and ( self.system_state ):
            self.move_state = False
            self.system_state = False

        if ( not msg.system_state ) and ( self.torque_enabled ) :
            self.pub_gripper_state.publish(Bool(True))

    def read_move_state(self,msg:Bool):
        if ( msg ) and ( self.move_state == False ):
            rospy.loginfo('[%10s] Move Enabled'%self.node_string)
            self.move_state = True
        if ( not msg ) and ( self.move_state == True):
            rospy.loginfo('[%10s] Move Disabled'%self.node_string)
            self.move_state = False

    def enable_torque(self):
        if ( not self.torque_enabled ):
            torque_enabled = False
            while not torque_enabled:
                torque_enabled = self.controller.MX28_start()
            self.pub_gripper_state.publish(Bool(True))
            rospy.loginfo('[%10s] Torque Enabled'%self.node_string)
            self.torque_enabled = True
           
    def read_target_force(self, msg:TargetForce):
        self.target_force = msg.target_force
  
    def read_sensor(self, msg:SensorState): 
        self.measured_gfZ = msg.gfZ
        self.critical_force()

    def read_target_delta(self, msg:TargetDelta):
        self.target_delta = msg.target_delta

    def write_target_position(self):
        if ( rospy.get_time() - self.prev_target_time > WRITE_FREQUENCY ):
            read_success = False
            while ( not read_success ):
                position = self.controller.MX28_pos()
                if ( type(position) != None ):
                    self.current_position = position
                    read_success = True

            if ( self.move_state == True ) : 
                if ( self.target_force == 0 ):
                    self.target_position = self.initial_position 
                elif ( np.abs(self.measured_gfZ - self.target_force) >= 0.25 ) :
                    self.target_position = self.current_position + self.target_delta

            elif ( self.move_state == False): 
                self.target_position = self.current_position 

            write_success = False
            self.writing_target = True
            while ( not write_success ):
                write_success = self.controller.MX28_target(int(self.target_position))
            self.prev_target_position = self.target_position
            self.writing_target = False
            self.prev_target_time = rospy.get_time()   
            
    def critical_force(self):
        if ( self.measured_gfZ > CRITICAL_FORCE ):
            self.controller.MX28_stop()
            self.critical_torque_limit = True
            self.move_enabled = False
            self.torque_enabled = False
            self.pub_gripper_state.publish(Bool(False))
            rospy.loginfo('[%10s] Critical force measured, torque disabled'%self.node_string)

    def shutdown(self, msg:Bool):
        if (msg.data):
            write_success = False
            while ( not write_success ):
                write_success = self.controller.MX28_stop()
            rospy.loginfo('[%10s] shutdown registered'%self.node_string)
            rospy.signal_shutdown('[%10s] shutdown registered'%self.node_string)

    def rosrun(self):
        while not rospy.is_shutdown():
            self.write_target_position()

class Gripper_idle():
    
    def __init__(self):
        self.node_string = 'Gripper'
        rospy.init_node('Gripper', anonymous=True)
        rospy.loginfo('[%10s] Starting %s'%( self.node_string, self.__class__.__name__))

        # Initialise the controller
        self.controller = MX28_Controller(port_num=COM_PORT, servo_id=SERVO_ID,resolution=SERVO_RESOLUTION,
                                             torque=MAX_SERVO_TORQUE,print_log=PRINT_LOG)

        # Initiate system variables
        self.torque_enabled = False
        self.system_state = False
        self.move_state = False
        
        # Initiate gripper position variables
        self.target_delta = 0
        self.target_force = 0
        self.current_position = 0
        self.target_position = 0
        self.prev_target_position = 0
        self.prev_target_time = 0

        # Initiate publishers
        self.pub_gripper_state = rospy.Publisher('gripper_state',Bool,queue_size=1)

        # Initiate subscribers
        self.sub_shutdown = rospy.Subscriber('shutdown',Bool,self.shutdown)
        self.sub_system_state = rospy.Subscriber('system_state',SystemState,self.read_system_state)
        self.sub_target_force = rospy.Subscriber('target_force',TargetForce,self.read_target_force)
        self.sub_sensor_state = rospy.Subscriber('/hub_0/sensor_0',SensorState,self.read_sensor)
        self.sub_target_delta = rospy.Subscriber('target_delta',TargetDelta,self.read_target_delta)
        self.sub_gripper_move_state = rospy.Subscriber('gripper_move_state',Bool,self.read_move_state)

        # Read current position
        read_success = False
        while ( not read_success ):
            position = self.controller.MX28_pos()
            if ( type(position) != None ):
                self.initial_position = position
                read_success = True

        self.enable_torque()
        self.rate = rospy.Rate(GRIPPER_RATE)
        self.rosrun()

    def read_system_state(self,msg:SystemState):
        if ( msg.system_state ) and ( not self.system_state ):
            rospy.loginfo('[%10s] System State: True'%self.node_string)
            self.move_state = True
            self.system_state = True

        elif ( not msg.system_state ) and ( self.system_state ):
            self.move_state = False
            self.system_state = False

        elif ( not msg.system_state ) and ( self.torque_enabled ) :
            self.pub_gripper_state.publish(Bool(True))

    def read_move_state(self,msg:Bool):
        if ( msg ) and ( self.move_state == False ):
            rospy.loginfo('[%10s] Move Enabled'%self.node_string)
            self.move_state = True
        if ( not msg ) and ( self.move_state == True):
            rospy.loginfo('[%10s] Move Disabled'%self.node_string)
            self.move_state = False

    def enable_torque(self):
        if ( not self.torque_enabled ):
            torque_enabled = False
            while not torque_enabled:
                torque_enabled = self.controller.MX28_start()
            self.pub_gripper_state.publish(Bool(True))
            rospy.loginfo('[%10s] Torque Enabled'%self.node_string)
            self.torque_enabled = True
           
    def read_target_force(self, msg:TargetForce):
        self.target_force = msg.target_force
  
    def read_sensor(self, msg:SensorState): 
        self.measured_gfZ = msg.gfZ
        self.critical_force()

    def read_target_delta(self, msg:TargetDelta):
        self.target_delta = msg.target_delta
            
    def critical_force(self):
        if ( self.measured_gfZ > CRITICAL_FORCE ):
            self.controller.MX28_stop()
            self.critical_torque_limit = True
            self.move_enabled = False
            self.torque_enabled = False
            self.pub_gripper_state.publish(Bool(False))
            rospy.loginfo('[%10s] Critical force measured, torque disabled'%self.node_string)

    def shutdown(self, msg:Bool):
        if (msg.data):
            write_success = False
            while ( not write_success ):
                write_success = self.controller.MX28_stop()
            rospy.loginfo('[%10s] shutdown registered'%self.node_string)
            rospy.signal_shutdown('[%10s] shutdown registered'%self.node_string)

    def rosrun(self):
        while not rospy.is_shutdown():
            rospy.sleep(1.)
    
class Gripper_Test_Idle():

    def __init__(self):
        rospy.init_node("Gripper", anonymous=True)
        rospy.loginfo('Starting Gripper Idle')


        # Initialisers
        self.init_node_time = rospy.get_time()
        self.init_gripper_time = 0
        self.init_gripper = False
        self.controller = MX28_Controller(port_num=COM_PORT, servo_id=SERVO_ID,resolution=SERVO_RESOLUTION,
                                             torque=MAX_SERVO_TORQUE,print_log=PRINT_LOG)

        # Variables
        self.mode = 'explore'
        self.explore_mode = True
        self.target_force = 0
        self.target_delta = 0
        self.measured_fZ = 0
        self.measured_time = self.init_node_time

        # Initiate condition variables
        self.torque_enabled = False
        self.move_enabled = False

        self.init_move_enabled = False
        self.writing_target = False
        self.critical_torque_limit = False
        self.prev_target_time = 0
        
        # Gripper variables
        self.current_position = 0
        self.target_position = 0
        self.prev_target_position = 0

        # Initiate publishers
        self.pub_gripper_state = rospy.Publisher('gripper_state',Bool,queue_size=1)

        # Initiate subscribers
        self.sub_shutdown = rospy.Subscriber('shutdown',Bool,self.shutdown)
        self.sub_system_state = rospy.Subscriber('system_state',SystemState,self.enable_torque)
        self.sub_gripper_move_state = rospy.Subscriber('gripper_move_state',Bool,self.enable_move)
        self.sub_target_force = rospy.Subscriber('target_force',TargetForce,self.read_target_force)
        self.sub_sensor_state = rospy.Subscriber('/hub_0/sensor_0',SensorState,self.read_sensor)
        self.sub_target_delta = rospy.Subscriber('target_delta',TargetDelta,self.read_target_delta)

        # self.enable_torque(Bool(True))
        self.rate = rospy.Rate(GRIPPER_RATE)
        self.rosrun()

    def read_system_state(self,msg:SystemState):
        if ( msg.sensor_state ) and ( msg.robot_state ) and ( not msg.gripper_state ) :
            self.enable_torque(Bool(True))

    def enable_torque(self, value):
        if ( value ) and ( not self.torque_enabled ):
            torque_enabled = False
            while not torque_enabled:
                torque_enabled = self.controller.MX28_start()
            self.pub_gripper_state.publish(Bool(True))
            rospy.loginfo('[gripper] Torque Enabled')
            self.torque_enabled = True
        else:
            self.pub_gripper_state.publish(Bool(True))
            rospy.loginfo('[gripper] Torque Enabled')

    def enable_move(self, msg:Bool):
        if ( msg ):
            self.move_enabled = True
        elif ( not msg ):
            self.move_enabled = False

    def read_target_force(self, msg:TargetForce):
        if self.move_enabled:
            self.target_force = msg.target_force    
    
    def read_sensor(self, msg:SensorState): 
        if self.move_enabled:
            self.measured_fZ = msg.gfZ
            self.measured_time = rospy.get_time()

            if (msg.is_contact) and (msg.gfZ >= 1):
                self.explore_mode = False
            elif (not msg.is_contact) and ( msg.gfZ < 1):
                self.explore_mode = True
            self.critical_force()

    def read_target_delta(self, msg:TargetDelta):
        if (self.move_enabled):
            self.target_delta = msg.target_delta

    def response_mode(self):

        if ( self.move_enabled ) and ( self.measured_time != self.init_node_time):
            
            if ( self.measured_fZ > MAX_FORCE ) and ( self.measured_fZ <= CRITICAL_FORCE ):
                self.mode = 'limit'

            elif ( self.measured_fZ > CRITICAL_FORCE ):
                self.mode = 'error'

            elif ( self.measured_fZ <= MAX_FORCE ) and ( self.explore_mode):
                self.mode = 'explore'

            elif ( self.measured_fZ <= MAX_FORCE ) and ( not self.explore_mode):
                self.mode = 'pid'

    def write_target_position(self):
        if ( self.move_enabled) :
            if ( self.mode == 'explore' ):
                if ( self.prev_target_position != CLOSE_LIMIT ):
                    self.target_position = CLOSE_LIMIT

            elif ( self.mode == 'error' ):
                if ( self.prev_target_position != OPEN_LIMIT ):
                    self.target_position = OPEN_LIMIT
                
            else:
                if (np.abs(self.measured_fZ - self.target_force) > FORCE_ACCURACY) and (not self.critical_torque_limit) and ( rospy.get_time() - self.prev_target_time > WRITE_FREQUENCY) :
                    read_success = False
                    while ( not read_success ):
                        position = self.controller.MX28_pos()
                        if ( type(position) != None ):
                            self.current_position = position
                            read_success = True
                    if ( self.mode == 'limit' ):
                        if (self.target_delta > 0 ):
                            self.target_position = position
                        else: 
                            self.target_position = self.target_delta + position
                        rospy.loginfo('[gripper] limit mode target: %d' % self.target_position)
                    else:
                        self.target_position = self.target_delta + position
                        rospy.loginfo('[gripper] pid mode target: %d' % self.target_position)
                        
            write_success = False
            self.writing_target = True
            while ( not write_success ):
                write_success = self.controller.MX28_target(int(self.target_position))
            self.prev_target_position = self.target_position
            self.writing_target = False
            self.prev_target_time = rospy.get_time()          

    def critical_force(self):
        if ( self.measured_fZ > CRITICAL_FORCE ):
            self.controller.MX28_stop()
            self.critical_torque_limit = True
            self.move_enabled = False
            self.torque_enabled = False
            self.pub_gripper_state.publish(Bool(False))
            rospy.loginfo('[gripper] Critical force measured, torque disabled')

    def shutdown(self, msg:Bool):
        write_success = False
        while ( not write_success ):
            write_success = self.controller.MX28_stop()
        rospy.loginfo('[gripper] shutdown registered')
        rospy.signal_shutdown('[gripper] shutdown registered')

    def rosrun(self):
        while not rospy.is_shutdown():
            self.response_mode()
            # self.write_target_position()

class GripperV1():

    def __init__(self):
        rospy.init_node("Gripper", anonymous=True)
        rospy.loginfo('Starting Gripper V1')

        # Initialisers
        self.init_node_time = rospy.get_time()
        self.init_gripper_time = 0
        self.init_gripper = False
        self.controller = MX28_Controller(port_num=COM_PORT, servo_id=SERVO_ID,resolution=SERVO_RESOLUTION,
                                             torque=MAX_SERVO_TORQUE,print_log=PRINT_LOG)

        # Variables
        self.mode = 'explore'
        self.explore_mode = True
        self.target_force = 0
        self.target_delta = 0
        self.measured_fZ = 0
        self.measured_time = self.init_node_time

        # Initiate condition variables
        self.torque_enabled = False
        self.move_enabled = False

        self.init_move_enabled = False
        self.writing_target = False
        self.critical_torque_limit = False
        self.prev_target_time = 0
        
        # Gripper variables
        self.current_position = 0
        self.target_position = 0
        self.prev_target_position = 0

        # Initiate publishers
        self.pub_gripper_state = rospy.Publisher('gripper_state',Bool,queue_size=1)

        # Initiate subscribers
        self.sub_shutdown = rospy.Subscriber('shutdown',Bool,self.shutdown)
        self.sub_system_state = rospy.Subscriber('system_state',SystemState,self.enable_torque)
        self.sub_gripper_move_state = rospy.Subscriber('gripper_move_state',Bool,self.enable_move)
        self.sub_target_force = rospy.Subscriber('target_force',TargetForce,self.read_target_force)
        self.sub_sensor_state = rospy.Subscriber('/hub_0/sensor_0',SensorState,self.read_sensor)
        self.sub_target_delta = rospy.Subscriber('target_delta',TargetDelta,self.read_target_delta)

        # self.enable_torque(Bool(True))
        self.rate = rospy.Rate(GRIPPER_RATE)
        self.rosrun()

    def read_system_state(self,msg:SystemState):
        if ( msg.sensor_state ) and ( msg.robot_state ) and ( not msg.gripper_state ) :
            self.enable_torque(Bool(True))

    def enable_torque(self, value):
        if ( value ) and ( not self.torque_enabled ):
            torque_enabled = False
            while not torque_enabled:
                torque_enabled = self.controller.MX28_start()
            self.pub_gripper_state.publish(Bool(True))
            rospy.loginfo('[gripper] Torque Enabled')
            self.torque_enabled = True

    def enable_move(self, msg:Bool):
        if ( msg ):
            self.move_enabled = True
        elif ( not msg ):
            self.move_enabled = False

    def read_target_force(self, msg:TargetForce):
        if self.move_enabled:
            self.target_force = msg.target_force    
    
    def read_sensor(self, msg:SensorState): 
        # if self.move_enabled:
            self.measured_fZ = msg.gfZ
            self.measured_time = rospy.get_time()

            if (msg.is_contact) and (msg.gfZ >= 1):
                self.explore_mode = False
            elif (not msg.is_contact) and ( msg.gfZ < 1):
                self.explore_mode = True
            self.critical_force()

    def read_target_delta(self, msg:TargetDelta):
        if (self.move_enabled):
            self.target_delta = msg.target_delta

    def response_mode(self):

        if ( self.move_enabled ) and ( self.measured_time != self.init_node_time):
            
            if ( self.measured_fZ > MAX_FORCE ) and ( self.measured_fZ <= CRITICAL_FORCE ):
                self.mode = 'limit'

            elif ( self.measured_fZ > CRITICAL_FORCE ):
                self.mode = 'error'

            elif ( self.measured_fZ < MAX_FORCE ) and ( self.explore_mode ):
                self.mode = 'explore'

            elif ( self.measured_fZ <= MAX_FORCE ) and ( not self.explore_mode):
                self.mode = 'pid'

    def write_target_position(self):
        if ( self.move_enabled ) :
            if ( self.mode == 'explore' ):
                if ( self.prev_target_position != CLOSE_LIMIT ):
                    self.target_position = CLOSE_LIMIT

            elif ( self.mode == 'error' ):
                if ( self.prev_target_position != OPEN_LIMIT ):
                    self.target_position = OPEN_LIMIT
                
            else:
                if (np.abs(self.measured_fZ - self.target_force) > FORCE_ACCURACY) and (not self.critical_torque_limit) and ( rospy.get_time() - self.prev_target_time > WRITE_FREQUENCY) :
                    read_success = False
                    while ( not read_success ):
                        position = self.controller.MX28_pos()
                        if ( type(position) != None ):
                            self.current_position = position
                            read_success = True
                    if ( self.mode == 'limit' ):
                        if (self.target_delta > 0 ):
                            self.target_position = position
                        else: 
                            self.target_position = self.target_delta + position
                        rospy.loginfo('[gripper] limit mode target: %d' % self.target_position)
                    else:
                        self.target_position = self.target_delta + position
                        rospy.loginfo('[gripper] pid mode target: %d' % self.target_position)
                        
            write_success = False
            self.writing_target = True
            while ( not write_success ):
                write_success = self.controller.MX28_target(int(self.target_position))
            self.prev_target_position = self.target_position
            self.writing_target = False
            self.prev_target_time = rospy.get_time()          

        elif ( self.torque_enabled ):
            if (not self.critical_torque_limit) and ( rospy.get_time() - self.prev_target_time > WRITE_FREQUENCY) :
 
                read_success = False
                while ( not read_success ):
                    position = self.controller.MX28_pos()
                    if ( type(position) != None ):
                        self.current_position = position
                        read_success = True
                if ( self.prev_target_position != self.current_position ):
                    write_success = False
                    self.writing_target = True
                    while ( not write_success ):
                        write_success = self.controller.MX28_target(int(self.current_position))
                    self.prev_target_position = self.current_position
                    self.writing_target = False
                    self.prev_target_time = rospy.get_time()  

    def critical_force(self):
        if ( self.measured_fZ > CRITICAL_FORCE ):
            self.controller.MX28_stop()
            self.critical_torque_limit = True
            self.move_enabled = False
            self.torque_enabled = False
            self.pub_gripper_state.publish(Bool(False))
            rospy.loginfo('[gripper] Critical force measured, torque disabled')

    def shutdown(self, msg:Bool):
        write_success = False
        while ( not write_success ):
            write_success = self.controller.MX28_stop()
        rospy.loginfo('[gripper] shutdown registered')
        rospy.signal_shutdown('[gripper] shutdown registered')

    def rosrun(self):
        while not rospy.is_shutdown():
            self.response_mode()
            self.write_target_position()

if __name__ == '__main__':
    try:
        hand = Gripper_idle()

    except rospy.ROSInterruptException:
        pass