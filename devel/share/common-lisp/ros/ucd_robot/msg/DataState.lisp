; Auto-generated. Do not edit!


(cl:in-package ucd_robot-msg)


;//! \htmlinclude DataState.msg.html

(cl:defclass <DataState> (roslisp-msg-protocol:ros-message)
  ((bias_state
    :reader bias_state
    :initarg :bias_state
    :type cl:boolean
    :initform cl:nil)
   (buffer_state
    :reader buffer_state
    :initarg :buffer_state
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass DataState (<DataState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DataState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DataState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ucd_robot-msg:<DataState> is deprecated: use ucd_robot-msg:DataState instead.")))

(cl:ensure-generic-function 'bias_state-val :lambda-list '(m))
(cl:defmethod bias_state-val ((m <DataState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ucd_robot-msg:bias_state-val is deprecated.  Use ucd_robot-msg:bias_state instead.")
  (bias_state m))

(cl:ensure-generic-function 'buffer_state-val :lambda-list '(m))
(cl:defmethod buffer_state-val ((m <DataState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ucd_robot-msg:buffer_state-val is deprecated.  Use ucd_robot-msg:buffer_state instead.")
  (buffer_state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DataState>) ostream)
  "Serializes a message object of type '<DataState>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'bias_state) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'buffer_state) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DataState>) istream)
  "Deserializes a message object of type '<DataState>"
    (cl:setf (cl:slot-value msg 'bias_state) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'buffer_state) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DataState>)))
  "Returns string type for a message object of type '<DataState>"
  "ucd_robot/DataState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DataState)))
  "Returns string type for a message object of type 'DataState"
  "ucd_robot/DataState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DataState>)))
  "Returns md5sum for a message object of type '<DataState>"
  "e4df093d868adffe6bda0f3e2ebd1f68")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DataState)))
  "Returns md5sum for a message object of type 'DataState"
  "e4df093d868adffe6bda0f3e2ebd1f68")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DataState>)))
  "Returns full string definition for message of type '<DataState>"
  (cl:format cl:nil "bool bias_state~%bool buffer_state~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DataState)))
  "Returns full string definition for message of type 'DataState"
  (cl:format cl:nil "bool bias_state~%bool buffer_state~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DataState>))
  (cl:+ 0
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DataState>))
  "Converts a ROS message object to a list"
  (cl:list 'DataState
    (cl:cons ':bias_state (bias_state msg))
    (cl:cons ':buffer_state (buffer_state msg))
))
