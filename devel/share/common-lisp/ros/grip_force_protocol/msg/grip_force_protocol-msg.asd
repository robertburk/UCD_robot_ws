
(cl:in-package :asdf)

(defsystem "grip_force_protocol-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "TargetForce" :depends-on ("_package_TargetForce"))
    (:file "_package_TargetForce" :depends-on ("_package"))
  ))