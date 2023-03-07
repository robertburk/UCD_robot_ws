; Auto-generated. Do not edit!


(cl:in-package ucd_robot-msg)


;//! \htmlinclude SystemState.msg.html

(cl:defclass <SystemState> (roslisp-msg-protocol:ros-message)
  ((system_state
    :reader system_state
    :initarg :system_state
    :type cl:boolean
    :initform cl:nil)
   (sensor_state
    :reader sensor_state
    :initarg :sensor_state
    :type cl:boolean
    :initform cl:nil)
   (gripper_state
    :reader gripper_state
    :initarg :gripper_state
    :type cl:boolean
    :initform cl:nil)
   (robot_state
    :reader robot_state
    :initarg :robot_state
    :type cl:boolean
    :initform cl:nil)
   (camera_state
    :reader camera_state
    :initarg :camera_state
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass SystemState (<SystemState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SystemState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SystemState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ucd_robot-msg:<SystemState> is deprecated: use ucd_robot-msg:SystemState instead.")))

(cl:ensure-generic-function 'system_state-val :lambda-list '(m))
(cl:defmethod system_state-val ((m <SystemState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ucd_robot-msg:system_state-val is deprecated.  Use ucd_robot-msg:system_state instead.")
  (system_state m))

(cl:ensure-generic-function 'sensor_state-val :lambda-list '(m))
(cl:defmethod sensor_state-val ((m <SystemState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ucd_robot-msg:sensor_state-val is deprecated.  Use ucd_robot-msg:sensor_state instead.")
  (sensor_state m))

(cl:ensure-generic-function 'gripper_state-val :lambda-list '(m))
(cl:defmethod gripper_state-val ((m <SystemState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ucd_robot-msg:gripper_state-val is deprecated.  Use ucd_robot-msg:gripper_state instead.")
  (gripper_state m))

(cl:ensure-generic-function 'robot_state-val :lambda-list '(m))
(cl:defmethod robot_state-val ((m <SystemState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ucd_robot-msg:robot_state-val is deprecated.  Use ucd_robot-msg:robot_state instead.")
  (robot_state m))

(cl:ensure-generic-function 'camera_state-val :lambda-list '(m))
(cl:defmethod camera_state-val ((m <SystemState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ucd_robot-msg:camera_state-val is deprecated.  Use ucd_robot-msg:camera_state instead.")
  (camera_state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SystemState>) ostream)
  "Serializes a message object of type '<SystemState>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'system_state) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'sensor_state) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'gripper_state) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'robot_state) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'camera_state) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SystemState>) istream)
  "Deserializes a message object of type '<SystemState>"
    (cl:setf (cl:slot-value msg 'system_state) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'sensor_state) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'gripper_state) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'robot_state) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'camera_state) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SystemState>)))
  "Returns string type for a message object of type '<SystemState>"
  "ucd_robot/SystemState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SystemState)))
  "Returns string type for a message object of type 'SystemState"
  "ucd_robot/SystemState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SystemState>)))
  "Returns md5sum for a message object of type '<SystemState>"
  "13c814d1fd4a9cbdec20374044113342")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SystemState)))
  "Returns md5sum for a message object of type 'SystemState"
  "13c814d1fd4a9cbdec20374044113342")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SystemState>)))
  "Returns full string definition for message of type '<SystemState>"
  (cl:format cl:nil "bool system_state ~%bool sensor_state~%bool gripper_state~%bool robot_state~%bool camera_state~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SystemState)))
  "Returns full string definition for message of type 'SystemState"
  (cl:format cl:nil "bool system_state ~%bool sensor_state~%bool gripper_state~%bool robot_state~%bool camera_state~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SystemState>))
  (cl:+ 0
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SystemState>))
  "Converts a ROS message object to a list"
  (cl:list 'SystemState
    (cl:cons ':system_state (system_state msg))
    (cl:cons ':sensor_state (sensor_state msg))
    (cl:cons ':gripper_state (gripper_state msg))
    (cl:cons ':robot_state (robot_state msg))
    (cl:cons ':camera_state (camera_state msg))
))
