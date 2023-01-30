#!/usr/bin/env python3
import rospy
import numpy as np
import pandas as pd
import random as rand

from std_msgs.msg import Bool
from ucd_robot.msg import DataState
from grip_force_protocol.msg import TargetForce
from papillarray_ros_v1.msg import SensorState

FORCE_ADAPTOR_NODE_RATE = 2000

class ConstTargetForceV1():

    def __init__(self):
        rospy.init_node('Grip Force Protocol', anonymous=True)
        rospy.loginfo('Starting ConstTargetForceV1')

        # Initialise variables and flags
        self.init_time= rospy.get_time()
        self.init_force_protocol = False

        self.explore_flag = 0
        self.prev_force = 0
        self.prev_publish_time = 0

        # Initiate Publishers
        self.pub_target_force = rospy.Publisher('target_force',TargetForce,queue_size=1)

        # Initiate Subscribers
        self.sub_shutdown = rospy.Subscriber('shutdown',Bool,self.shutdown)
        self.sub_data_state = rospy.Subscriber('data_state',DataState,self.enable_force_protocol)
        self.sub_sensor_state = rospy.Subscriber('/hub_0/sensor_0',SensorState,self.read_measured_force)

        self.rate = rospy.Rate(FORCE_ADAPTOR_NODE_RATE)
        self.rosrun()

    def enable_force_protocol(self, msg:DataState):
        self.init_force_protocol = True
        rospy.loginfo('[grip_force_protocol] Conditions met, node enabled')

    def read_measured_force(self, msg:SensorState):
        self.measured_force = msg.gfZ

    def set_target_force(self):

        if self.init_force_protocol:
            target_force = TargetForce()

            if (self.prev_force == 0):
                target_force.target_force = 25
                self.prev_force = 25
                            
            else:
                if (rospy.get_time() - self.prev_publish_time > 5):
                    target_force.target_force = self.prev_force
                    target_force.target_force = rand.uniform(8,30)
                    rospy.loginfo('New target force: %d', target_force.target_force)
                    self.prev_publish_time = rospy.get_time()
                    self.prev_force = target_force.target_force
                else:
                    target_force.target_force = self.prev_force

            self.pub_target_force.publish(target_force)

    def shutdown(self, msg:Bool):
        rospy.loginfo('[grip_force_protocol] shutdown registered')
        rospy.signal_shutdown('[grip_force_protocol] shutdown registered')

    def rosrun(self):
        while not rospy.is_shutdown():
            self.set_target_force()

if __name__ == '__main__':
    try:
        hand = ConstTargetForceV1()

    except rospy.ROSInterruptException:
        pass