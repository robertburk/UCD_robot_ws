;; Auto-generated. Do not edit!


(when (boundp 'ucd_robot::DataState)
  (if (not (find-package "UCD_ROBOT"))
    (make-package "UCD_ROBOT"))
  (shadow 'DataState (find-package "UCD_ROBOT")))
(unless (find-package "UCD_ROBOT::DATASTATE")
  (make-package "UCD_ROBOT::DATASTATE"))

(in-package "ROS")
;;//! \htmlinclude DataState.msg.html


(defclass ucd_robot::DataState
  :super ros::object
  :slots (_bias_state _buffer_state ))

(defmethod ucd_robot::DataState
  (:init
   (&key
    ((:bias_state __bias_state) nil)
    ((:buffer_state __buffer_state) nil)
    )
   (send-super :init)
   (setq _bias_state __bias_state)
   (setq _buffer_state __buffer_state)
   self)
  (:bias_state
   (&optional (__bias_state :null))
   (if (not (eq __bias_state :null)) (setq _bias_state __bias_state)) _bias_state)
  (:buffer_state
   (&optional (__buffer_state :null))
   (if (not (eq __buffer_state :null)) (setq _buffer_state __buffer_state)) _buffer_state)
  (:serialization-length
   ()
   (+
    ;; bool _bias_state
    1
    ;; bool _buffer_state
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _bias_state
       (if _bias_state (write-byte -1 s) (write-byte 0 s))
     ;; bool _buffer_state
       (if _buffer_state (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _bias_state
     (setq _bias_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _buffer_state
     (setq _buffer_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get ucd_robot::DataState :md5sum-) "e4df093d868adffe6bda0f3e2ebd1f68")
(setf (get ucd_robot::DataState :datatype-) "ucd_robot/DataState")
(setf (get ucd_robot::DataState :definition-)
      "bool bias_state
bool buffer_state
")



(provide :ucd_robot/DataState "e4df093d868adffe6bda0f3e2ebd1f68")


