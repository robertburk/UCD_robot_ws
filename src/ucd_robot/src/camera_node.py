#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the camera node, which continuously records images. It's important to 
note that the frame rate (FPS) is not determined by the node itself, but by the
 sensor reader. The camera node listens for data sequences from the sensor reader,
 and when it receives one, it records an image. This is done to ensure that the
 camera's timing aligns with that of the sensor reader.
"""
import numpy as np
import warnings
import time
import os
import rospy
import cv2
import pyrealsense2 as rs

from papillarray_ros_v2.msg import SensorState
from std_msgs.msg import Bool
from ucd_robot.msg import SystemState

warnings.filterwarnings("ignore")


'''
Modify this if you want to make the image clearer.
'''
width = 640
heigth = 480


'''
It is important!!!!!!!!!!!!!!!! to note that you may need to modify the port 
number to ensure that it is pointing to the correct port for loading the 
intelrealsensor camera. The allocation of the port may be random (as it is on my PC) 
or it can be deterministic. It is recommended that you test it to confirm.
You can use the 'camera_test.py to confirm it if you want to'
'''
port_num = 6

class RealSenseCamera_Idle():
    def __init__(self):
        self.node_string = 'RealSense'
        rospy.init_node('Camera', anonymous=True)
        rospy.loginfo('[%10s] Starting %s'%( self.node_string, self.__class__.__name__))

        # Initiate Flags 
        self.camera_ready = False
        self.system_state = False

        # Initiate camera Variables
        
        pipeline = rs.pipeline()
        config = rs.config()
        config.enable_stream(rs.stream.color, width, heigth, rs.format.bgr8, 30)
        pipeline.start(config)
        align_to = rs.stream.color
        align = rs.align(align_to)
        frames = pipeline.wait_for_frames()
        aligned_frames = align.process(frames)
        color_frame = aligned_frames.get_color_frame()
        intr = color_frame.profile.as_video_stream_profile().intrinsics
        intr_matrix = np.array([
            [intr.fx, 0, intr.ppx], [0, intr.fy, intr.ppy], [0, 0, 1]
        ])
        pipeline.stop()
        params = {}
        params['matrix'] = intr_matrix
        params['coeffs'] = np.array(intr.coeffs)
        
        self.camera = cv2.VideoCapture(port_num)
        self.camera.set(3, width)  # width=1920
        self.camera.set(4, heigth)  # height=1080

        self.images = {}
        self.data = {}
        self.data['params'] = params
        self.save_t = None
        self.save_name = 'TestSave'

        # Initialise Publishers & Subscribers
        self.pub_camera_state = rospy.Publisher('camera_state',Bool,queue_size=1)
        self.sub_shutdown = rospy.Subscriber('shutdown',Bool,self.shutdown)
        self.sub_system_state = rospy.Subscriber('system_state',SystemState,self.read_system_state)
        self.sub_sensor_state = rospy.Subscriber('/hub_0/sensor_0',SensorState, self.update)

        self.init_camera()
        self.rosrun()

    def init_camera(self):
        '''
        This function is crucial because the camera needs to be initialized 
        through several steps the first time it's used after starting up. 
        Otherwise, the initial frames captured may not be clear.
        '''
        for i in range(100):
            self.camera.read()

        self.camera_ready = True
        self.pub_camera_state.publish(self.camera_ready)
    
    def read_system_state(self,msg:SystemState):
        if ( msg.system_state ) and ( not self.system_state ):
            rospy.loginfo('[%10s] System State: True'%self.node_string)
            self.system_state = True

        elif ( not msg.system_state ) and ( self.system_state ):
            rospy.loginfo('[%10s] System State: False'%(self.node_string))
            self.system_state = False

    def update(self, msg:SensorState):
        if (self.system_state):
            t = msg.tus
            ret, color_image = self.camera.read()
            self.images[f'{t}'] = color_image
            save_successful = False
            while not save_successful:
                save_successful =  self.save_data()
            # rospy.signal_shutdown('[%10s] shutdown registered'%self.node_string)


    def save_data(self):
        '''
        If it doesn't already exist, create a directory named "results" in the
        root path of this project. Then, store the image data and camera parameters
        in a file named "images.npy". It's important to note that this file
        doesn't just include the images, but also the camera parameters, which
        are used for calibrating the Aruco marker.
        '''
        self.data['images'] = self.images
        save_path = '/home/rob/UCD_robot_ws_v2/src/ucd_robot/images/images_data'
        # if not os.path.exists(save_path):
        #     os.makedirs(save_path)
        # print(f'saving to {save_path}/images.npy')
        # np.save(f'{save_path}/images.npy', self.data)
        return True
    
    def shutdown(self, msg:Bool):
        if ( msg.data ) :
            rospy.loginfo('[%10s] shutdown registered'%self.node_string)
            rospy.signal_shutdown('[%10s] shutdown registered'%self.node_string)

    def rosrun(self):
        while not rospy.is_shutdown():
            rospy.sleep(0.5)

if __name__ == '__main__':
    try:
        detector_ros = RealSenseCamera_Idle()
    except rospy.ROSInterruptException:
        pass