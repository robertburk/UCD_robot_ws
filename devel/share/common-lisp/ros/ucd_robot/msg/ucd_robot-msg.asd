
(cl:in-package :asdf)

(defsystem "ucd_robot-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "DataState" :depends-on ("_package_DataState"))
    (:file "_package_DataState" :depends-on ("_package"))
  ))