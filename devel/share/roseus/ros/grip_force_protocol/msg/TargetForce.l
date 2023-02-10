;; Auto-generated. Do not edit!


(when (boundp 'grip_force_protocol::TargetForce)
  (if (not (find-package "GRIP_FORCE_PROTOCOL"))
    (make-package "GRIP_FORCE_PROTOCOL"))
  (shadow 'TargetForce (find-package "GRIP_FORCE_PROTOCOL")))
(unless (find-package "GRIP_FORCE_PROTOCOL::TARGETFORCE")
  (make-package "GRIP_FORCE_PROTOCOL::TARGETFORCE"))

(in-package "ROS")
;;//! \htmlinclude TargetForce.msg.html


(defclass grip_force_protocol::TargetForce
  :super ros::object
  :slots (_target_force ))

(defmethod grip_force_protocol::TargetForce
  (:init
   (&key
    ((:target_force __target_force) 0.0)
    )
   (send-super :init)
   (setq _target_force (float __target_force))
   self)
  (:target_force
   (&optional __target_force)
   (if __target_force (setq _target_force __target_force)) _target_force)
  (:serialization-length
   ()
   (+
    ;; float32 _target_force
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _target_force
       (sys::poke _target_force (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _target_force
     (setq _target_force (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get grip_force_protocol::TargetForce :md5sum-) "e0e0e39f568c9ce1104c278640a8f08d")
(setf (get grip_force_protocol::TargetForce :datatype-) "grip_force_protocol/TargetForce")
(setf (get grip_force_protocol::TargetForce :definition-)
      "float32 target_force
")



(provide :grip_force_protocol/TargetForce "e0e0e39f568c9ce1104c278640a8f08d")


