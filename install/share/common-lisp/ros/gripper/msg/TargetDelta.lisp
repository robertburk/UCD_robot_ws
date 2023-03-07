; Auto-generated. Do not edit!


(cl:in-package gripper-msg)


;//! \htmlinclude TargetDelta.msg.html

(cl:defclass <TargetDelta> (roslisp-msg-protocol:ros-message)
  ((target_delta
    :reader target_delta
    :initarg :target_delta
    :type cl:float
    :initform 0.0))
)

(cl:defclass TargetDelta (<TargetDelta>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TargetDelta>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TargetDelta)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gripper-msg:<TargetDelta> is deprecated: use gripper-msg:TargetDelta instead.")))

(cl:ensure-generic-function 'target_delta-val :lambda-list '(m))
(cl:defmethod target_delta-val ((m <TargetDelta>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gripper-msg:target_delta-val is deprecated.  Use gripper-msg:target_delta instead.")
  (target_delta m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TargetDelta>) ostream)
  "Serializes a message object of type '<TargetDelta>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'target_delta))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TargetDelta>) istream)
  "Deserializes a message object of type '<TargetDelta>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_delta) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TargetDelta>)))
  "Returns string type for a message object of type '<TargetDelta>"
  "gripper/TargetDelta")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TargetDelta)))
  "Returns string type for a message object of type 'TargetDelta"
  "gripper/TargetDelta")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TargetDelta>)))
  "Returns md5sum for a message object of type '<TargetDelta>"
  "7f44729b36d41b3490ff1e46feb4d3a0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TargetDelta)))
  "Returns md5sum for a message object of type 'TargetDelta"
  "7f44729b36d41b3490ff1e46feb4d3a0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TargetDelta>)))
  "Returns full string definition for message of type '<TargetDelta>"
  (cl:format cl:nil "float32 target_delta~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TargetDelta)))
  "Returns full string definition for message of type 'TargetDelta"
  (cl:format cl:nil "float32 target_delta~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TargetDelta>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TargetDelta>))
  "Converts a ROS message object to a list"
  (cl:list 'TargetDelta
    (cl:cons ':target_delta (target_delta msg))
))
