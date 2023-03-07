;; Auto-generated. Do not edit!


(when (boundp 'gripper_force_adaptor::TargetForce)
  (if (not (find-package "GRIPPER_FORCE_ADAPTOR"))
    (make-package "GRIPPER_FORCE_ADAPTOR"))
  (shadow 'TargetForce (find-package "GRIPPER_FORCE_ADAPTOR")))
(unless (find-package "GRIPPER_FORCE_ADAPTOR::TARGETFORCE")
  (make-package "GRIPPER_FORCE_ADAPTOR::TARGETFORCE"))

(in-package "ROS")
;;//! \htmlinclude TargetForce.msg.html


(defclass gripper_force_adaptor::TargetForce
  :super ros::object
  :slots (_target_force ))

(defmethod gripper_force_adaptor::TargetForce
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

(setf (get gripper_force_adaptor::TargetForce :md5sum-) "e0e0e39f568c9ce1104c278640a8f08d")
(setf (get gripper_force_adaptor::TargetForce :datatype-) "gripper_force_adaptor/TargetForce")
(setf (get gripper_force_adaptor::TargetForce :definition-)
      "float32 target_force
")



(provide :gripper_force_adaptor/TargetForce "e0e0e39f568c9ce1104c278640a8f08d")


