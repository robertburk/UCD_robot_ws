#!/usr/bin/env python3
import rospy
import numpy as np
import pandas as pd

from std_msgs.msg import Bool
from papillarray_ros_v2.msg import SensorState
from papillarray_ros_v2.srv import BiasRequest, StartSlipDetection, StopSlipDetection
from ucd_robot.msg import SystemState
from gripper.msg import TargetForce
from tf2_msgs.msg import TFMessage
import geometry_msgs.msg as geometry_msgs

UCD_ROBOT_RATE = 1000
BUFFER_LENGTH = 500
TEST_LENGTH_TIME = 60 # [seconds]
SENSOR_DELAY_TIME = 0.5
TEST_TIME = 5 # hold each position for 5 seconds
NUMBER_TESTS = 1
MIN_GRIP_FORCE = 4
MAX_GRIP_FORCE = 20

class UCDRobot_exp1():

        def __init__(self):
            
            self.node_string = 'UCD Robot'
            rospy.init_node('UCD Robot', anonymous=True)
            rospy.loginfo('[%10s] Starting %s'%( self.node_string, self.__class__.__name__))

            # Initialise variables and flags
            self.init_time = rospy.get_time()
            self.init_ucd_robot_time = 0
            self.init_ucd_robot = False

            # Initiate hardware flags
            self.sensor_connect = False
            self.bias_state = False
            self.buffer_state = False
            self.sensor_state = False
            self.robot_state = True
            self.gripper_state = False
            self.camera_state = False
            self.system_state = False

            # Initiate Variables
            self.i = 0
            self.measured_gfZ = 0 
            self.prev_sensor_read = 0
            self.init_z = -1
            self.z = 0

            # Initiate publishers
            self.pub_shutdown = rospy.Publisher('shutdown',Bool,queue_size=1)
            self.pub_system_state = rospy.Publisher('system_state',SystemState,queue_size=1)
            self.pub_gripper_move_state = rospy.Publisher('gripper_move_state',Bool,queue_size=1)

            # Initiate controlling publishers
            self.pub_target_force = rospy.Publisher('target_force',TargetForce, queue_size=1)
            self.pub_target_pose = rospy.Publisher('target_pose',geometry_msgs.Pose, queue_size=1)

            # Initiate subscribers
            self.sub_sensor_state = rospy.Subscriber('/hub_0/sensor_0',SensorState,self.read_sensor_state)
            self.sub_robot_state = rospy.Subscriber('robot_state',Bool,self.read_robot_state)
            self.sub_gripper_state = rospy.Subscriber('gripper_state',Bool,self.read_gripper_state)
            self.sub_camera_state = rospy.Subscriber('camera_state',Bool,self.read_camera_state)
            self.sub_program_running = rospy.Subscriber('/ur_hardware_interface/robot_program_running',Bool,self.read_robot_state)
            self.sub_joint_state = rospy.Subscriber('tf',TFMessage, self.read_joint_state)

            self.rate = rospy.Rate(UCD_ROBOT_RATE)
            self.rosrun()

        def request_bias(self):
            rospy.wait_for_service("/hub_" + "0" + "/send_bias_request")
            bias_serv = rospy.ServiceProxy("/hub_" + "0" + "/send_bias_request",BiasRequest)
            resp = bias_serv.call()
            if resp.result:
                self.bias_state = True
                rospy.loginfo('[%10s] System Check: bias state %s'%( self.node_string, self.bias_state))
            else:
                raise RuntimeError('Bias sensor error')

        def system_check(self):
            if ( self.sensor_state ) and ( self.robot_state ) and ( self.gripper_state ) and ( self.camera_state ) and ( not self.system_state ):
                rospy.loginfo('[%10s] System State: True'%(self.node_string))
                system_state = SystemState()
                system_state.robot_state = True
                system_state.gripper_state = True
                system_state.sensor_state = True
                self.camera_state = True
                system_state.system_state = True
                self.pub_system_state.publish(system_state)
                self.system_state = True

            elif (not self.sensor_state) or ( not self.robot_state ) or ( not self.gripper_state ) or ( not self.camera_state ):
                if ( self.system_state ) :
                    if ( not self.sensor_state ):
                        rospy.loginfo('[%10s] Sensor State: %s'%(self.node_string,self.sensor_state))
                        self.system_state = False
                    if ( not self.robot_state ):
                        rospy.loginfo('[%10s Robot State: %s'%(self.node_string,self.robot_state))
                        self.system_state = False
                    if ( not self.gripper_state ):
                        rospy.loginfo('[%10s] Gripper State: %s'%(self.node_string,self.gripper_state))
                        self.system_state = False
                    if ( not self.camera_state ):
                        rospy.loginfo('[%10s] Camera State: %s'%(self.node_string,self.camera_state))
                        self.system_state = False

                system_state = SystemState()
                system_state.robot_state = self.robot_state
                system_state.gripper_state = self.gripper_state
                system_state.sensor_state = self.sensor_state
                system_state.camera_state = self.camera_state
                system_state.system_state = self.system_state
                self.pub_system_state.publish(system_state)

            else: 
                system_state = SystemState()
                system_state.system_state = self.system_state
                system_state.robot_state = self.robot_state
                system_state.gripper_state = self.gripper_state
                system_state.sensor_state = self.sensor_state
                system_state.camera_state = self.camera_state
                self.pub_system_state.publish(system_state)

        def read_robot_state(self, msg:Bool):
            if ( msg.data ) and ( not self.robot_state ):
                rospy.loginfo('[%10s] Robot Connected'%self.node_string)
                self.robot_state = True
            elif ( not msg.data ) and ( self.robot_state ):
                rospy.loginfo('[%10s] Robot Disconnected'%self.node_string)       
                self.robot_state = False

        def read_gripper_state(self, msg:Bool):
            if ( msg.data ) and ( not self.gripper_state ):
                rospy.loginfo('[%10s] Gripper Connected'%self.node_string)
                self.gripper_state = True
            elif ( not msg.data ) and ( self.gripper_state ):
                rospy.loginfo('[%10s] Gripper Disconnected'%self.node_string)
                self.gripper_state = False

        def read_sensor_state(self, msg:SensorState):

            if ( not self.sensor_connect ):
                rospy.loginfo('[%10s] Sensor Connected'%self.node_string)
                self.request_bias()
                self.sensor_connect = True

            if ( self.bias_state ) :
                self.i += 1

            if ( self.i > BUFFER_LENGTH ) and ( not self.buffer_state ):
                rospy.loginfo('[%10s] Buffer State: true'%self.node_string)
                self.buffer_state = True
            
            if ( self.buffer_state ) and ( self.bias_state ) and ( not self.sensor_state ):
                rospy.loginfo('[%10s] Sensor Ready'%self.node_string)
                self.sensor_state = True

            if ( self.system_state ):
                self.measured_gfZ = msg.gfZ
            
            self.prev_sensor_read = rospy.get_time()

        def read_camera_state(self,msg:Bool):
            if ( msg.data ) and ( not self.camera_state ):
                rospy.loginfo('[%10s] Camera Connected'%self.node_string)
                self.camera_state = True

            elif ( not msg.data ) and ( self.camera_state ):
                rospy.loginfo('[%10s] Camera Disconnected'%(self.node_string))
                self.camera_state = False

        def read_joint_state(self, msg:TFMessage):
            if ( self.init_z == -1 ) :
                if (msg.transforms[0].transform.translation.z != 0 ) :
                    self.init_z = msg.transforms[0].transform.translation.z
            
            if (msg.transforms[0].transform.translation.z != 0 ) :
                self.z = msg.transforms[0].transform.translation.z
    
        def experimental_procedure(self):

            self.exp_string = 'EXP PRTCL'

            grip_forces = np.linspace(MIN_GRIP_FORCE,MAX_GRIP_FORCE,9,endpoint=True)

            rospy.loginfo('[%10s] Experiment Begun'%self.exp_string)
            self.experiment_start_time = rospy.get_time()
            for j in range(NUMBER_TESTS):
                rospy.loginfo('[%10s] Beginning test %d'%(self.exp_string,j))
                for k in (grip_forces):                    
                    user_choice = 0 # 0 = ask, 1 = continue, -1 = stop
                    # continue_test
                    while user_choice == 0:
                        input_str = input('Continue with test, next grip force: %d? (1 = Yes, 0 = Stop)'%k)
                        try:
                            choice = int(input_str)
                            if ( choice == 1):
                                rospy.loginfo('[%10s] User input: 1, continuing test'%self.exp_string)
                                user_choice = 1
                            elif ( choice == 0 ):
                                rospy.loginfo('[%10s] User input: 0, stopping test'%self.exp_string)
                                user_choice == -1
                            else:
                                rospy.loginfo('[%10s] User input invalid'%self.exp_string)
                        except ValueError:
                            rospy.loginfo("Input is not a valid number. Please try again.")

                    rospy.loginfo('[%10s] Beginning grip force %d'%(self.exp_string,k))
                    self.target_force = k
                    # Apply grip force 
                    self.pub_gripper_move_state.publish(Bool(True))
                    while ( np.abs( self.target_force - self.measured_gfZ ) >= 0.3 ):
                        target_force = TargetForce()
                        target_force.target_force = float(k)
                        self.pub_target_force.publish(target_force)
                    rospy.loginfo("[%10s] Measured: %f target: %f"%(self.exp_string,self.measured_gfZ, self.target_force))
                    self.pub_gripper_move_state.publish(Bool(False))

                    # Move robot
                    rospy.loginfo('[%10s] Instructing robot to raise'%self.exp_string)
                    up_pose = geometry_msgs.Pose(
                        geometry_msgs.Vector3(0, 0, 0.01), geometry_msgs.Quaternion(0, 0, 0, 0)
                    )
                    self.pub_target_pose.publish(up_pose)
                    while ( np.abs(self.z - self.init_z) < 0.008 ):
                        print('up',np.abs(self.z - self.init_z) )
                        rospy.sleep(1.)
                    
                    rospy.loginfo('[%10s] Robot raised'%(self.exp_string))
                    
                    self.test_start_time = rospy.get_time()

                    # Maintain grip for 5 seconds

                    while ( np.abs(rospy.get_time() - self.test_start_time) < 5): 
                        rospy.sleep(1.)

                    rospy.loginfo('[%10s] instructing robot to lower'%(self.exp_string))
                    
                    # Move robot
                    down_pose = geometry_msgs.Pose(
                        geometry_msgs.Vector3(0, 0, -0.01), geometry_msgs.Quaternion(0, 0, 0, 0)
                    )
                    self.pub_target_pose.publish(down_pose)

                    while ( np.abs(self.z - self.init_z) > 0.002 ):
                        print('down',np.abs(self.z - self.init_z))
                        rospy.sleep(1.)
                    rospy.loginfo('[%10s] robot lowered'%(self.exp_string))

                    # Open Gripper 
                    self.pub_gripper_move_state.publish(Bool(True))
                    while ( self.measured_gfZ > 0.25 ):
                        target_force = TargetForce()
                        target_force.target_force = 0
                        self.pub_target_force.publish(target_force)
                    self.pub_gripper_move_state.publish(Bool(False))

                    while not self.bias_state:
                        self.request_bias()

                    rospy.loginfo('[%10s] Grip force %s complete'%(self.exp_string,k))

                    rospy.sleep(5.)

                rospy.loginfo('[%10s] Test %d complete'%(self.exp_string,j))
            rospy.loginfo('[%10s] Experiment Complete'%self.exp_string)
                 
        def rosrun(self):
            while ( self.system_state == False ):
                self.system_check()
            
            self.experimental_procedure()
          
class UCDRobotV1():

        def __init__(self):
            rospy.init_node("UCDRobot", anonymous=True)
            rospy.loginfo('Starting UCDRobot V1')

            # Initialise init variables
            self.init_node_time = rospy.get_time()
            self.init_ucd_robot_time = 0
            self.init_ucd_robot = False


            # Initiate node variables
            self.i = 0 # number of sensor samples read in
            self.contact_state = False
            self.slip_request = False
            self.prev_sensor_time = rospy.get_time()

            # Initiate publishers
            self.pub_shutdown = rospy.Publisher('shutdown',Bool,queue_size=1)
            self.pub_system_state = rospy.Publisher('system_state',SystemState,queue_size=1)
            self.pub_gripper_move_state = rospy.Publisher('gripper_move_state',Bool,queue_size=1)

            # Initiate subscribers
            self.sub_sensor_state = rospy.Subscriber('/hub_0/sensor_0',SensorState,self.read_sensor_state)
            self.sub_robot_state = rospy.Subscriber('robot_state',Bool,self.read_robot_state)
            self.sub_gripper_state = rospy.Subscriber('gripper_state',Bool,self.read_gripper_state)
            self.sub_program_running = rospy.Subscriber('/ur_hardware_interface/robot_program_running',Bool,self.read_robot_state)

            # Initiate system flags
            self.bias_state = False
            self.buffer_state = False
            self.sensor_state = False
            self.robot_state = False
            self.gripper_state = False

            while self.bias_state == False:
                self.request_bias()

            self.rate = rospy.Rate(UCD_ROBOT_RATE)
            self.rosrun()

        def request_bias(self):
            rospy.wait_for_service("/hub_" + "0" + "/send_bias_request")
            bias_serv = rospy.ServiceProxy("/hub_" + "0" + "/send_bias_request",BiasRequest)
            resp = bias_serv.call()
            if resp.result:
                rospy.loginfo('[ucd_robot] System Check: bias request complete')
                self.bias_state = True
                return True
            else:
                raise RuntimeError('Bias sensor error')

        def system_check(self):
            if ( self.sensor_state ) and ( self.gripper_state ) and ( self.robot_state ):
                if ( not self.init_ucd_robot ):
                    self.init_ucd_robot_time = rospy.get_time()
                    rospy.loginfo('[ucd_robot] System ready, ucd robot enabled')
                    self.init_ucd_robot_time = rospy.get_time()
                    system_state = SystemState()
                    system_state.system_state = True
                    system_state.sensor_state = True
                    system_state.gripper_state = True
                    system_state.robot_state = True
                    self.pub_system_state.publish(system_state)
                    self.init_ucd_robot = True
            
            else: 
                system_state = SystemState()
                system_state.system_state = False
                system_state.sensor_state = self.sensor_state
                system_state.gripper_state = self.gripper_state
                system_state.robot_state = self.robot_state
                self.pub_system_state.publish(system_state)
                if ( self.init_ucd_robot ):
                    self.init_ucd_robot = False

        def read_robot_state(self, msg:Bool):
            if ( msg.data):
                self.robot_state = True
                rospy.loginfo('[ucd_robot] System Check: robot ready')

            elif ( not msg.data ):
                self.robot_state = False
                rospy.loginfo('[ucd_robot] System Check: robot offline')

        def read_gripper_state(self, msg:Bool):
            if ( msg ):
                self.gripper_state = True
                rospy.loginfo('[ucd_robot] System Check: gripper ready')

            elif ( not msg ):
                self.gripper_state = False                
                rospy.loginfo('[ucd_robot] System Check: gripper offline')

        def read_sensor_state(self, msg:SensorState):

            self.prev_sensor_time = rospy.get_time()

            # Wait for conditions to be met before initiating the system
            if not self.init_ucd_robot:

                if self.i >= BUFFER_LENGTH and ( not self.buffer_state ) and ( self.bias_state ):# Data conditions met, enable the force calculations and PID control
                    rospy.loginfo('[ucd_robot] System Check: buffer length met')
                    self.buffer_state = True
                
            if ( self.init_ucd_robot) and ( msg.is_contact ) and ( not self.contact_state ):
                self.slip_request = True
                rospy.wait_for_service("/hub_" + "0" + "/start_slip_detection")
                slip_det = rospy.ServiceProxy("/hub_" + "0" + "/start_slip_detection",StartSlipDetection)
                slip = slip_det.call()
                if slip.result:
                    rospy.loginfo('[ucd_robot] System Check: slip detection started')
                    self.slip_detection_state = True
                else:
                    raise RuntimeError('Slip Detection Request error')
                self.contact_state = True

            elif ( self.init_ucd_robot) and ( not msg.is_contact ) and ( self.contact_state ) and msg.gfZ < 1:
                self.slip_request = False
                rospy.wait_for_service("/hub_" + "0" + "/stop_slip_detection")
                slip_det = rospy.ServiceProxy("/hub_" + "0" + "/stop_slip_detection",StopSlipDetection)
                slip = slip_det.call()
                if slip.result:
                    rospy.loginfo('[ucd_robot] System Check: slip detection stopped')
                    self.slip_detection_state = False
                else:
                    raise RuntimeError('Bias sensor error')
                self.contact_state = False

            self.sensor_monit()
            self.i += 1

        def sensor_monit(self):
            if ( not self.init_ucd_robot ):
                self.prev_sensor_time = rospy.get_time()

            elif ( self.init_ucd_robot) and ( rospy.get_time() - self.prev_sensor_time > SENSOR_DELAY_TIME) and (not rospy.is_shutdown()):# and (not self.slip_request):
                shutdown = Bool(True)
                self.pub_shutdown.publish(shutdown)
                rospy.loginfo('[ucd_robot] Error: sensor latency > %.2f s' % SENSOR_DELAY_TIME)
                rospy.signal_shutdown('[ucd_robot] Error: sensor latency > %.2f s' % SENSOR_DELAY_TIME)

            if ( self.bias_state ) and ( self.buffer_state ) and ( not self.sensor_state ):
                self.sensor_state = True

        def rosrun(self):
            while not rospy.is_shutdown():
                while ( self.init_ucd_robot == False ):
                    self.system_check()
                if (self.init_ucd_robot ) and ( rospy.get_time() - self.init_ucd_robot_time > TEST_LENGTH_TIME ):
                    shutdown = Bool(True)
                    self.pub_shutdown.publish(shutdown)      
                    rospy.loginfo('[ucd_robot] Test Complete (Duration: %d)' % TEST_LENGTH_TIME)  
                    rospy.signal_shutdown('[ucd_robot] Test Complete (Duration: %d' % TEST_LENGTH_TIME)

                self.sensor_monit()

if __name__ == '__main__':
    try:
        hand = UCDRobot_exp1()

    except rospy.ROSInterruptException:
        pass