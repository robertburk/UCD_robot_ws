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
FORCE_ACCURACY = 0.01 # Accepted force accuracy: +/- 0.01N

class ContactileTargetForceV1():

    def __init__(self):
        rospy.init_node('Grip Force Protocol', anonymous=True)
        rospy.loginfo('Starting ConstTargetForceV1')

        # Initialise variables and flags
        self.init_time= rospy.get_time()
        self.init_force_protocol = False

        self.explore_mode = 1
        self.slip_state = 0
        self.slip_mode = 0 # 0 = not slipping | 1 = uncompensated slip | 2 = slipping and increasing force 
        self.prev_force = 0
        self.prev_publish_time = 0
        self.sensor_target_force = 0 
        self.target_force = 0

        # Initiate Publishers
        self.pub_target_force = rospy.Publisher('target_force',TargetForce,queue_size=1)

        # Initiate Subscribers
        self.sub_shutdown = rospy.Subscriber('shutdown',Bool,self.shutdown)
        self.sub_data_state = rospy.Subscriber('data_state',DataState,self.enable_force_protocol)
        self.sub_sensor_state = rospy.Subscriber('/hub_0/sensor_0',SensorState,self.read_sensor_force)

        self.rate = rospy.Rate(FORCE_ADAPTOR_NODE_RATE)
        self.rosrun()

    def enable_force_protocol(self, msg:DataState):
        self.init_force_protocol = True
        rospy.loginfo('[grip_force_protocol] Conditions met, node enabled')

    def read_sensor_force(self, msg:SensorState):

        self.measured_force = msg.gfZ
        
        if ( self.explore_mode == 1 and msg.is_contact ):
            self.explore_mode = 0

        elif ( self.explore_mode == 0 and not msg.is_contact and msg.gfZ < 2 ):
            self.explore_mode = 1
        
        if ( msg.is_contact and msg.is_sd_active):
            self.sensor_target_force = msg.target_grip_force
        else:
            self.sensor_target_force = -1


    def set_target_force(self):

        if self.init_force_protocol:
            target_force = TargetForce()
            target_force.target_force = self.target_force

            if ( self.explore_mode ) or ( self.sensor_target_force == -1):
                self.target_force = 10
                target_force.target_force = self.target_force
                            
            else:
                target_force.target_force = self.sensor_target_force

            self.pub_target_force.publish(target_force)
            self.prev_force = self.target_force

    def shutdown(self, msg:Bool):
        rospy.loginfo('[grip_force_protocol] shutdown registered')
        rospy.signal_shutdown('[grip_force_protocol] shutdown registered')

    def rosrun(self):
        while not rospy.is_shutdown():
            self.set_target_force()

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
                target_force.target_force = 24
                self.prev_force = 24
                            
            else:
                if (rospy.get_time() - self.prev_publish_time > 3):
                    target_force.target_force = self.prev_force
                    integ = rand.randint(0,1)
                    if ( integ == 0 ):
                        target_force.target_force -= 4
                    elif ( integ == 1):
                        target_force.target_force += 4

                    if (target_force.target_force == 48 ) or (target_force.target_force == 4):
                        target_force.target_force = 24

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
        hand = ContactileTargetForceV1()

    except rospy.ROSInterruptException:
        pass