#!/usr/bin/env python3
import rospy
import numpy as np
import pandas as pd
from simple_pid import PID

from std_msgs.msg import Bool
from papillarray_ros_v1.msg import SensorState
from papillarray_ros_v1.srv import BiasRequest
from ucd_robot.msg import DataState
from MX28_node import MX28_Controller
from grip_force_protocol.msg import TargetForce
from gripper_position_controller.msg import TargetDelta

# Constants
DELTA_LIMIT = 82 # Estimated maximum movement per MX28 loop
OUTPUT_INTERVAL = 0.01 # Min. time between new target forces
OPEN_LIMIT = -28000
CLOSE_LIMIT = 28000
MAX_FORCE = 50
CRITICAL_FORCE = MAX_FORCE + 5
FORCE_ACCURACY = 0.01 # Accepted force accuracy: +/- 0.05N
POSITION_ACCURACY = 2
WRITE_FREQUENCY = 0.05

MAX_SERVO_TORQUE = 1023
SERVO_RESOLUTION = 1
PRINT_LOG = 1
COM_PORT= "/dev/ttyUSB0"
SERVO_ID = 1


GRIPPER_RATE = 1000

class GripperV1():

    def __init__(self):
        rospy.init_node("Gripper", anonymous=True)
        rospy.loginfo('Starting Gripper V1')

        # Initialisers
        self.init_time = rospy.get_time()
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
        self.measured_time = self.init_time

        # Initiate condition variables
        self.init_move_enabled = False
        self.writing_target = False
        self.critical_torque_limit = False
        self.prev_target_time = 0
        
        # Gripper variables
        self.current_position = 0
        self.target_position = 0
        self.prev_target_position = 0

        # Initiate publishers

        # Initiate subscribers
        self.sub_shutdown = rospy.Subscriber('shutdown',Bool,self.shutdown)
        self.sub_data_state = rospy.Subscriber('data_state',DataState,self.enable_torque)
        self.sub_target_force = rospy.Subscriber('target_force',TargetForce,self.read_target_force)
        self.sub_sensor_state = rospy.Subscriber('/hub_0/sensor_0',SensorState,self.read_sensor)
        self.sub_target_delta = rospy.Subscriber('target_delta',TargetDelta,self.read_target_delta)

        self.rate = rospy.Rate(GRIPPER_RATE)
        self.rosrun()

    def enable_torque(self, msg:DataState):
        self.controller.MX28_start()
        self.init_move_enabled = True
        rospy.loginfo('[gripper] Conditions met, node enabled')

    def read_target_force(self, msg:TargetForce):
        if self.init_move_enabled:
            self.target_force = msg.target_force    
    
    def read_sensor(self, msg:SensorState): 
        if self.init_move_enabled:
            self.measured_fZ = msg.gfZ
            self.measured_time = rospy.get_time()

            if (msg.is_contact) and (msg.gfZ >= 4):
                self.explore_mode = False
            elif (not msg.is_contact) and ( msg.gfZ < 4):
                self.explore_mode = True
            self.critical_torque()

    def read_target_delta(self, msg:TargetDelta):
        if (self.init_move_enabled):
            self.target_delta = msg.target_delta

    def response_mode(self):

        if ( self.init_move_enabled ) and ( self.measured_time != self.init_time):
            
            if ( self.measured_fZ > MAX_FORCE ) and ( self.measured_fZ <= CRITICAL_FORCE ):
                self.mode = 'limit'

            elif ( self.measured_fZ > CRITICAL_FORCE ):
                self.mode = 'error'

            elif ( self.measured_fZ <= MAX_FORCE ) and ( self.explore_mode):
                self.mode = 'explore'

            elif ( self.measured_fZ <= MAX_FORCE ) and ( not self.explore_mode):
                self.mode = 'pid'

    def set_target_position(self):
        if ( self.init_move_enabled) :
            if ( self.mode == 'explore' ):
                if ( self.prev_target_position != CLOSE_LIMIT ):
                    self.target_position = CLOSE_LIMIT
                    rospy.loginfo('[gripper] explore mode target: %d' % self.target_position)

            elif ( self.mode == 'error' ):
                if ( self.prev_target_position != OPEN_LIMIT ):
                    self.target_position = OPEN_LIMIT
                    rospy.loginfo('[gripper] error mode target: %d' % self.target_position)

            else:
                if np.abs(self.measured_fZ - self.target_force) > FORCE_ACCURACY and not self.critical_torque_limit:
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
                        
            self.write_target_position()

    def write_target_position(self):

        if ( rospy.get_time() - self.prev_target_time > WRITE_FREQUENCY and not self.critical_torque_limit) :
            write_success = False
            self.writing_target = True
            while ( not write_success ):
                write_success = self.controller.MX28_target(int(self.target_position))
            # write_success = False
            self.prev_target_position = self.target_position
            self.writing_target = False
            self.prev_target_time = rospy.get_time()            

    def set_target_position_v2(self):
        if ( self.init_move_enabled) :
            if ( self.mode == 'explore' ):
                if ( self.prev_target_position != CLOSE_LIMIT ):
                    self.target_position = CLOSE_LIMIT
                    rospy.loginfo('[gripper] explore mode target: %d' % self.target_position)

            elif ( self.mode == 'error' ):
                if ( self.prev_target_position != OPEN_LIMIT ):
                    self.target_position = OPEN_LIMIT
                    rospy.loginfo('[gripper] error mode target: %d' % self.target_position)

            else:
                if np.abs(self.measured_fZ - self.target_force) > FORCE_ACCURACY and not self.critical_torque_limit:
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
                        
            self.write_target_position_v2()

    def write_target_position_v2(self):
        if ( self.init_move_enabled) :
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


    def critical_torque(self):
        if ( self.measured_fZ > CRITICAL_FORCE ):
            self.critical_torque_limit = True
            self.init_move_enabled = False
            self.controller.MX28_stop()

    def shutdown(self, msg:Bool):
        write_success = False
        while ( not write_success ):
            write_success = self.controller.MX28_stop()
        rospy.loginfo('[gripper] shutdown registered')
        rospy.signal_shutdown('[gripper] shutdown registered')

    def rosrun(self):
        while not rospy.is_shutdown():
            self.response_mode()
            self.set_target_position()

    def rosrun_v2(self):
        while not rospy.is_shutdown():
            self.response_mode()
            self.write_target_position()

if __name__ == '__main__':
    try:
        hand = GripperV1()

    except rospy.ROSInterruptException:
        pass