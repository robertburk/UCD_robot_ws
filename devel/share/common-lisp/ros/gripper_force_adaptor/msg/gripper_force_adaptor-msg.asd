
(cl:in-package :asdf)

(defsystem "gripper_force_adaptor-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "TargetForce" :depends-on ("_package_TargetForce"))
    (:file "_package_TargetForce" :depends-on ("_package"))
  ))