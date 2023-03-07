
(cl:in-package :asdf)

(defsystem "gripper-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "TargetDelta" :depends-on ("_package_TargetDelta"))
    (:file "_package_TargetDelta" :depends-on ("_package"))
  ))