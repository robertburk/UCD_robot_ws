#!/usr/bin/env python3
import rospy
import numpy as np
import pandas as pd

from std_msgs.msg import Bool
from papillarray_ros_v1.msg import SensorState
from papillarray_ros_v1.srv import BiasRequest, StartSlipDetection

import time

class UCDRobotV1():

        def __init__(self):
            rospy.init_node("UCDRobot", anonymous=True)
            rospy.loginfo('Starting UCDRobot V1')
            self.contact_state = False
            self.sub_sensor_state = rospy.Subscriber('/hub_0/sensor_0',SensorState,self.response_mode)

            rospy.wait_for_service("/hub_" + "0" + "/send_bias_request")
            bias_serv = rospy.ServiceProxy("/hub_" + "0" + "/send_bias_request",BiasRequest)
            resp = bias_serv.call()
            if resp.result:
                rospy.loginfo('[ucd_robot] System Check: bias request complete')
                self.bias_state = True
            else:
                raise RuntimeError('Bias sensor error')   
            self.rate = rospy.Rate(1000)
            self.rosrun()   

        def response_mode(self, msg:SensorState):

            self.prev_sensor_time = rospy.get_time()

            if ( msg.is_contact ) and ( not self.contact_state ):
                rospy.wait_for_service("/hub_" + "0" + "/start_slip_detection")
                slip_det = rospy.ServiceProxy("/hub_" + "0" + "/start_slip_detection",StartSlipDetection)
                slip = slip_det.call()
                if slip.result:
                    rospy.loginfo('[ucd_robot] System Check: slip detection started')
                    self.bias_state = True
                else:
                    raise RuntimeError('Bias sensor error')
                self.contact_state = True
                    
        def rosrun(self):
            while True:
                self.rate.sleep()

if __name__ == '__main__':
    try:
        hand = UCDRobotV1()

    except rospy.ROSInterruptException:
        pass