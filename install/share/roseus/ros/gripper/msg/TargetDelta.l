;; Auto-generated. Do not edit!


(when (boundp 'gripper::TargetDelta)
  (if (not (find-package "GRIPPER"))
    (make-package "GRIPPER"))
  (shadow 'TargetDelta (find-package "GRIPPER")))
(unless (find-package "GRIPPER::TARGETDELTA")
  (make-package "GRIPPER::TARGETDELTA"))

(in-package "ROS")
;;//! \htmlinclude TargetDelta.msg.html


(defclass gripper::TargetDelta
  :super ros::object
  :slots (_target_delta ))

(defmethod gripper::TargetDelta
  (:init
   (&key
    ((:target_delta __target_delta) 0.0)
    )
   (send-super :init)
   (setq _target_delta (float __target_delta))
   self)
  (:target_delta
   (&optional __target_delta)
   (if __target_delta (setq _target_delta __target_delta)) _target_delta)
  (:serialization-length
   ()
   (+
    ;; float32 _target_delta
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _target_delta
       (sys::poke _target_delta (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _target_delta
     (setq _target_delta (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get gripper::TargetDelta :md5sum-) "7f44729b36d41b3490ff1e46feb4d3a0")
(setf (get gripper::TargetDelta :datatype-) "gripper/TargetDelta")
(setf (get gripper::TargetDelta :definition-)
      "float32 target_delta
")



(provide :gripper/TargetDelta "7f44729b36d41b3490ff1e46feb4d3a0")


