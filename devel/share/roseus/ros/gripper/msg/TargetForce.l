;; Auto-generated. Do not edit!


(when (boundp 'gripper::TargetForce)
  (if (not (find-package "GRIPPER"))
    (make-package "GRIPPER"))
  (shadow 'TargetForce (find-package "GRIPPER")))
(unless (find-package "GRIPPER::TARGETFORCE")
  (make-package "GRIPPER::TARGETFORCE"))

(in-package "ROS")
;;//! \htmlinclude TargetForce.msg.html


(defclass gripper::TargetForce
  :super ros::object
  :slots (_target_force ))

(defmethod gripper::TargetForce
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

(setf (get gripper::TargetForce :md5sum-) "e0e0e39f568c9ce1104c278640a8f08d")
(setf (get gripper::TargetForce :datatype-) "gripper/TargetForce")
(setf (get gripper::TargetForce :definition-)
      "float32 target_force
")



(provide :gripper/TargetForce "e0e0e39f568c9ce1104c278640a8f08d")


