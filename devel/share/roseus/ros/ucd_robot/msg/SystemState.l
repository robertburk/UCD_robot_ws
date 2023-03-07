;; Auto-generated. Do not edit!


(when (boundp 'ucd_robot::SystemState)
  (if (not (find-package "UCD_ROBOT"))
    (make-package "UCD_ROBOT"))
  (shadow 'SystemState (find-package "UCD_ROBOT")))
(unless (find-package "UCD_ROBOT::SYSTEMSTATE")
  (make-package "UCD_ROBOT::SYSTEMSTATE"))

(in-package "ROS")
;;//! \htmlinclude SystemState.msg.html


(defclass ucd_robot::SystemState
  :super ros::object
  :slots (_system_state _sensor_state _gripper_state _robot_state _camera_state ))

(defmethod ucd_robot::SystemState
  (:init
   (&key
    ((:system_state __system_state) nil)
    ((:sensor_state __sensor_state) nil)
    ((:gripper_state __gripper_state) nil)
    ((:robot_state __robot_state) nil)
    ((:camera_state __camera_state) nil)
    )
   (send-super :init)
   (setq _system_state __system_state)
   (setq _sensor_state __sensor_state)
   (setq _gripper_state __gripper_state)
   (setq _robot_state __robot_state)
   (setq _camera_state __camera_state)
   self)
  (:system_state
   (&optional (__system_state :null))
   (if (not (eq __system_state :null)) (setq _system_state __system_state)) _system_state)
  (:sensor_state
   (&optional (__sensor_state :null))
   (if (not (eq __sensor_state :null)) (setq _sensor_state __sensor_state)) _sensor_state)
  (:gripper_state
   (&optional (__gripper_state :null))
   (if (not (eq __gripper_state :null)) (setq _gripper_state __gripper_state)) _gripper_state)
  (:robot_state
   (&optional (__robot_state :null))
   (if (not (eq __robot_state :null)) (setq _robot_state __robot_state)) _robot_state)
  (:camera_state
   (&optional (__camera_state :null))
   (if (not (eq __camera_state :null)) (setq _camera_state __camera_state)) _camera_state)
  (:serialization-length
   ()
   (+
    ;; bool _system_state
    1
    ;; bool _sensor_state
    1
    ;; bool _gripper_state
    1
    ;; bool _robot_state
    1
    ;; bool _camera_state
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _system_state
       (if _system_state (write-byte -1 s) (write-byte 0 s))
     ;; bool _sensor_state
       (if _sensor_state (write-byte -1 s) (write-byte 0 s))
     ;; bool _gripper_state
       (if _gripper_state (write-byte -1 s) (write-byte 0 s))
     ;; bool _robot_state
       (if _robot_state (write-byte -1 s) (write-byte 0 s))
     ;; bool _camera_state
       (if _camera_state (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _system_state
     (setq _system_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _sensor_state
     (setq _sensor_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _gripper_state
     (setq _gripper_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _robot_state
     (setq _robot_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _camera_state
     (setq _camera_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get ucd_robot::SystemState :md5sum-) "13c814d1fd4a9cbdec20374044113342")
(setf (get ucd_robot::SystemState :datatype-) "ucd_robot/SystemState")
(setf (get ucd_robot::SystemState :definition-)
      "bool system_state 
bool sensor_state
bool gripper_state
bool robot_state
bool camera_state
")



(provide :ucd_robot/SystemState "13c814d1fd4a9cbdec20374044113342")


