#!/usr/bin/env python3
import rospy
import numpy as np
from simple_pid import PID

from std_msgs.msg import Bool
from ucd_robot.msg import SystemState
from gripper.msg import TargetForce
from papillarray_ros_v2.msg import SensorState
from gripper.msg import TargetDelta

POSITION_CONTROLLER_NODE_RATE = 1000

# Constants
DELTA_LIMIT = 82 # Estimated maximum movement per MX28 loop
OUTPUT_INTERVAL = 0.001 # Min. time between new target forces
OPEN_LIMIT = -28000
CLOSE_LIMIT = 28000
FORCE_ACCURACY = 0.01 # Accepted force accuracy: +/- 0.01N

PID_P = 25 #10
PID_I = 0.4 #
PID_D = 0

class PIDController():

    def __init__(self):

        self.node_string = 'PID Node'
        rospy.init_node('Delta Position Controller', anonymous=True)
        rospy.loginfo('[%10s] Starting %s'%( self.node_string, self.__class__.__name__))

        # Initialise state variables
        self.system_state = False

        # Initialise Variables
        self.measured_fZ = 0
        self.target_force = 0
        self.pid = PID(PID_P, PID_I, PID_D,sample_time=0.001,output_limits=(-2*DELTA_LIMIT,2*DELTA_LIMIT))

        # Initiate Publishers
        self.pub_target_delta = rospy.Publisher('target_delta',TargetDelta,queue_size=1)

        # Initiate Subscribers
        self.sub_shutdown = rospy.Subscriber('shutdown',Bool,self.shutdown)
        self.sub_system_state = rospy.Subscriber('system_state',SystemState,self.read_system_state)
        self.sub_target_force = rospy.Subscriber('target_force',TargetForce,self.read_target_force)
        self.sub_sensor_state = rospy.Subscriber('/hub_0/sensor_0',SensorState,self.read_measured_fZ)

        self.rate = rospy.Rate(POSITION_CONTROLLER_NODE_RATE)
        self.rosrun()

    def read_system_state(self, msg:SystemState):
        if ( msg.system_state ) and ( not self.system_state ):
            rospy.loginfo('[%10s] System State: True'%self.node_string)
            self.system_state = True

        elif ( not msg.system_state ) and ( self.system_state ):
            rospy.loginfo('[%10s] System State: False'%self.node_string)
            self.system_state = False

    def read_measured_fZ(self, msg:SensorState):
        if ( self.system_state):
            self.measured_fZ = msg.gfZ

    def read_target_force(self, msg:TargetForce):
        if ( self.system_state):
            self.pid.setpoint = msg.target_force
            self.target_force = msg.target_force   

    def PID_controller(self):
        if ( self.system_state):
            if np.abs(self.measured_fZ - self.target_force) > FORCE_ACCURACY:
                self.target_delta = self.pid(self.measured_fZ)
                target_delta = TargetDelta()
                target_delta.target_delta = self.target_delta
                self.pub_target_delta.publish(target_delta) 

    def shutdown(self, msg:Bool):
        if (msg.data):
            rospy.loginfo('[%10s] shutdown registered'%self.node_string )
            rospy.signal_shutdown('[%10s] shutdown registered'%self.node_string )

    def rosrun(self):
        while not rospy.is_shutdown():
            self.PID_controller()

if __name__ == '__main__':
    try:
        hand = PIDController()

    except rospy.ROSInterruptException:
        pass