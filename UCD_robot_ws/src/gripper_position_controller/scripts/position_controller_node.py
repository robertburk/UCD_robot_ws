#!/usr/bin/env python3
import rospy
import numpy as np
import pandas as pd
import random as rand
from simple_pid import PID

from std_msgs.msg import Bool
from ucd_robot.msg import DataState
from grip_force_protocol.msg import TargetForce
from papillarray_ros_v1.msg import SensorState
from gripper_position_controller.msg import TargetDelta

POSITION_CONTROLLER_NODE_RATE = 1000

# Constants
DELTA_LIMIT = 82 # Estimated maximum movement per MX28 loop
OUTPUT_INTERVAL = 0.001 # Min. time between new target forces
OPEN_LIMIT = -28000
CLOSE_LIMIT = 28000
FORCE_ACCURACY = 0.01 # Accepted force accuracy: +/- 0.05N

PID_P = 50 #10
PID_I = 0 #
PID_D = 0

class DeltaPositionControllerV1():

    def __init__(self):
        rospy.init_node('Delta Position Controller', anonymous=True)
        rospy.loginfo('Starting DeltaPositionControllerV1')

        # Initialise variables and flags
        self.init_time= rospy.get_time()
        self.init_position_controller = False

        self.explore_flag = 0
        self.prev_delta = 0
        self.prev_publish_time = 0

        self.measured_fZ = 0
        self.target_force = 0

        # Initiate Publishers
        self.pub_target_delta = rospy.Publisher('target_delta',TargetDelta,queue_size=1)

        # Initiate Subscribers
        self.sub_shutdown = rospy.Subscriber('shutdown',Bool,self.shutdown)
        self.sub_data_state = rospy.Subscriber('data_state',DataState,self.enable_position_controller)
        self.sub_target_force = rospy.Subscriber('target_force',TargetForce,self.read_target_force)
        self.sub_sensor_state = rospy.Subscriber('/hub_0/sensor_0',SensorState,self.read_measured_fZ)

        self.pid = PID(PID_P, PID_I, PID_D,sample_time=0.001,output_limits=(-DELTA_LIMIT,DELTA_LIMIT))

        self.rate = rospy.Rate(POSITION_CONTROLLER_NODE_RATE)
        self.rosrun()

    def enable_position_controller(self, msg:DataState):
        if ( msg.bias_state and msg.buffer_state):
            self.init_position_controller = True
            rospy.loginfo('[position_controller_node] Conditions met, node enabled')    
        
    def read_measured_fZ(self, msg:SensorState):
        if ( self.init_position_controller):
            self.measured_fZ = msg.gfZ

    def read_target_force(self, msg:TargetForce):
        if ( self.init_position_controller):
            self.pid.setpoint = msg.target_force
            self.target_force = msg.target_force   

    def PID_controller(self):
        if ( self.init_position_controller):
            if np.abs(self.measured_fZ - self.target_force) > FORCE_ACCURACY:
                self.target_delta = self.pid(self.measured_fZ)
                target_delta = TargetDelta()
                target_delta.target_delta = self.target_delta
                self.pub_target_delta.publish(target_delta) 

    def shutdown(self, msg:Bool):
        rospy.loginfo('[position_controller_node] shutdown registered')
        rospy.signal_shutdown('[position_controller_node] shutdown registered')

    def rosrun(self):
        while not rospy.is_shutdown():
            self.PID_controller()

if __name__ == '__main__':
    try:
        hand = DeltaPositionControllerV1()

    except rospy.ROSInterruptException:
        pass