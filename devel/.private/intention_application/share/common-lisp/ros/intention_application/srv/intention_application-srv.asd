
(cl:in-package :asdf)

(defsystem "intention_application-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "snapshot" :depends-on ("_package_snapshot"))
    (:file "_package_snapshot" :depends-on ("_package"))
  ))