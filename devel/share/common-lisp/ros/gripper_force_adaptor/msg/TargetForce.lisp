; Auto-generated. Do not edit!


(cl:in-package gripper_force_adaptor-msg)


;//! \htmlinclude TargetForce.msg.html

(cl:defclass <TargetForce> (roslisp-msg-protocol:ros-message)
  ((target_force
    :reader target_force
    :initarg :target_force
    :type cl:float
    :initform 0.0))
)

(cl:defclass TargetForce (<TargetForce>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TargetForce>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TargetForce)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gripper_force_adaptor-msg:<TargetForce> is deprecated: use gripper_force_adaptor-msg:TargetForce instead.")))

(cl:ensure-generic-function 'target_force-val :lambda-list '(m))
(cl:defmethod target_force-val ((m <TargetForce>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gripper_force_adaptor-msg:target_force-val is deprecated.  Use gripper_force_adaptor-msg:target_force instead.")
  (target_force m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TargetForce>) ostream)
  "Serializes a message object of type '<TargetForce>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'target_force))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TargetForce>) istream)
  "Deserializes a message object of type '<TargetForce>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'target_force) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TargetForce>)))
  "Returns string type for a message object of type '<TargetForce>"
  "gripper_force_adaptor/TargetForce")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TargetForce)))
  "Returns string type for a message object of type 'TargetForce"
  "gripper_force_adaptor/TargetForce")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TargetForce>)))
  "Returns md5sum for a message object of type '<TargetForce>"
  "e0e0e39f568c9ce1104c278640a8f08d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TargetForce)))
  "Returns md5sum for a message object of type 'TargetForce"
  "e0e0e39f568c9ce1104c278640a8f08d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TargetForce>)))
  "Returns full string definition for message of type '<TargetForce>"
  (cl:format cl:nil "float32 target_force~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TargetForce)))
  "Returns full string definition for message of type 'TargetForce"
  (cl:format cl:nil "float32 target_force~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TargetForce>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TargetForce>))
  "Converts a ROS message object to a list"
  (cl:list 'TargetForce
    (cl:cons ':target_force (target_force msg))
))
