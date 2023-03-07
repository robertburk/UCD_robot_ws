#!/usr/bin/env python
# license removed for brevity
import sys  
from Robotic_Servos import openport,openpacket,Robotis_Servo
import pandas as pd
import math
'''
This is the main class you can use for controling the gripper, for the up-to-date
version, there are just a few functions you can use, but you can self-customize
your own funcstions based on 'Robotic_Servo'.
'''

class MX28_Controller():
    '''
    Important!!!!!!!!!!!!!!!!!!!!!
    Notice: Please calibarate the gripper before using this code
    '''

    def __init__(self, port_num, servo_id,torque,resolution=1,print_log=False):
        '''
        port_num: port on your PC that connect with the servo, you can check it from system's device manager
        id: servo's ID, you can check it from dymanixel wizard
        '''
        self.id = servo_id
        self.port_num = port_num
        self.port = openport(port_num)
        self.packet = openpacket()
        self.servo = Robotis_Servo(self.port, self.packet, self.id)
        self.servo.init_multiturn_mode()
        # print('Setting resolution to: ', resolution)
        self.servo.set_resolution(resolution)
        self.servo.set_return_delay_time(0)
        self.print_log = print_log
        self.mode = 'multiturn'
        self.servo.set_torque(torque)
        df = pd.DataFrame(pd.read_csv('/home/rob/UCD_robot_ws/src/gripper/scripts/calibration.csv'))
        
        self.close_limit = int(df['close_limit']-100)
        self.open_limit = int(df['open_limit'])+100
        
    def MX28_target(self, target):
        success = self.servo.moveit(target, self.mode)
        # success = True
        if self.print_log and success:
            # print("Gripper is moving to %d" %target)
            return True
            
    def MX28_close(self,speed=100):
        if speed == 0:
            self.MX28_stop()
            print("Gripper is stopped")
        else:
            # self.servo.multiturn_set_speed(math.ceil(speed))
            self.servo.moveit(self.close_limit)
            if self.print_log:
                print("Gripper is closing")

    def MX28_open(self,speed=100):
        if speed == 0:
            self.MX28_stop()
            print("Gripper is stopped")
        else:
            # self.servo.multiturn_set_speed(math.ceil(speed))
            self.servo.moveit(self.open_limit)
            if self.print_log:
                print("Gripper is opening")
      
    def MX28_speed(self):
        return self.servo.read_speed()
    
    def MX28_load(self):
        return self.servo.read_load()

    def MX28_goal(self):
        return self.servo.read_goal()
    
    def MX28_pos(self):
        return self.servo.read_current_pos()

    def MX28_load(self):
        load = self.servo.read_load()
        if load != None and load > 50:
            self.MX28_stop()
        return load

    def MX28_stop(self):  # TODO: another way to rewrite this
        #stop the servo anytime
        self.servo.disable_torque()
        # self.servo.enable_torque()
        
    def MX28_start(self):  # TODO: another way to rewrite this
        #stop the servo anytime
        # self.servo.disable_torque()
        self.servo.enable_torque()
        # print('Torque enabled')
        return True
        
    
        

