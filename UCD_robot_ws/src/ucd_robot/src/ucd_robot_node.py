#!/usr/bin/env python3
import rospy
import numpy as np
import pandas as pd

from std_msgs.msg import Bool
from papillarray_ros_v1.msg import SensorState
from papillarray_ros_v1.srv import BiasRequest
from ucd_robot.msg import DataState

UCD_ROBOT_RATE = 1000
BUFFER_LENGTH = 1100
TEST_LENGTH_TIME = 60
SENSOR_DELAY_TIME = 0.1

class structtype():
    pass

class UCDRobotV1():

        def __init__(self):
            rospy.init_node("UCDRobot", anonymous=True)
            rospy.loginfo('Starting UCDRobot V1')

            # Initialise variables and flags
            self.init_time = rospy.get_time()
            self.init_ucd_robot_time = 0
            self.init_ucd_robot = False

            # Initiate publishers
            self.pub_data_state = rospy.Publisher('data_state',DataState,queue_size=1)
            self.pub_shutdown = rospy.Publisher('shutdown',Bool,queue_size=1)

            # Initiate subscribers
            self.sub_sensor_state = rospy.Subscriber('/hub_0/sensor_0',SensorState,self.response_mode)

            # Initiate condition variables
            self.i = 0 # number of sensor samples read in
            self.bias_state = False
            self.buffer_state = False
            self.prev_sensor_time = rospy.get_time()

            # Make bias request
            rospy.wait_for_service("/hub_" + "0" + "/send_bias_request")
            bias_serv = rospy.ServiceProxy("/hub_" + "0" + "/send_bias_request",BiasRequest)
            resp = bias_serv.call()
            if resp.result:
                rospy.loginfo('[ucd_robot] System Check: bias request complete')
                self.bias_state = True
            else:
                raise RuntimeError('Bias sensor error')

            self.rate = rospy.Rate(UCD_ROBOT_RATE)
            self.rosrun()

        def response_mode(self, msg:SensorState):

            self.prev_sensor_time = rospy.get_time()
            # Wait for conditions to be met before initiating the system
            if not self.init_ucd_robot:

                if self.i >= BUFFER_LENGTH:# Data conditions met, enable the force calculations and PID control
                    rospy.loginfo('[ucd_robot] System Check: buffer length met')
                    self.buffer_state = True
                    data_state = DataState()
                    data_state.bias_state = self.bias_state
                    data_state.buffer_state = self.buffer_state
                    self.pub_data_state.publish(data_state)
                    rospy.loginfo('[ucd_robot] Conditions met, node enabled')
                    self.init_ucd_robot_time = rospy.get_time()
                    self.init_ucd_robot = True

            # elif self.init_ucd_robot:

            #     # Safety checks
            #     pass

            self.i += 1

        def sensor_state(self):
            if ( not self.init_ucd_robot ):
                self.prev_sensor_time = rospy.get_time()

            elif ( self.init_ucd_robot) and ( rospy.get_time() - self.prev_sensor_time > SENSOR_DELAY_TIME) and (not rospy.is_shutdown()):
                shutdown = Bool(True)
                self.pub_shutdown.publish(shutdown)
                rospy.loginfo('[ucd_robot] Error: sensor latency > %.2f s' % SENSOR_DELAY_TIME)
                rospy.signal_shutdown('[ucd_robot] Error: sensor latency > %.2f s' % SENSOR_DELAY_TIME)

        def rosrun(self):
            while not rospy.is_shutdown():
                if (self.init_ucd_robot ) and ( rospy.get_time() - self.init_ucd_robot_time > TEST_LENGTH_TIME ):

                    shutdown = Bool(True)
                    self.pub_shutdown.publish(shutdown)      
                    rospy.loginfo('[ucd_robot] Test Complete (Duration: %d)' % TEST_LENGTH_TIME)  
                    rospy.signal_shutdown('[ucd_robot] Test Complete (Duration: %d' % TEST_LENGTH_TIME)

                self.sensor_state()
        #     self.rate.sleep()

if __name__ == '__main__':
    try:
        hand = UCDRobotV1()

    except rospy.ROSInterruptException:
        pass