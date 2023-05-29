;; Auto-generated. Do not edit!


(when (boundp 'intention_application::Array)
  (if (not (find-package "INTENTION_APPLICATION"))
    (make-package "INTENTION_APPLICATION"))
  (shadow 'Array (find-package "INTENTION_APPLICATION")))
(unless (find-package "INTENTION_APPLICATION::ARRAY")
  (make-package "INTENTION_APPLICATION::ARRAY"))

(in-package "ROS")
;;//! \htmlinclude Array.msg.html


(defclass intention_application::Array
  :super ros::object
  :slots (_x _y _intention ))

(defmethod intention_application::Array
  (:init
   (&key
    ((:x __x) 0)
    ((:y __y) 0)
    ((:intention __intention) nil)
    )
   (send-super :init)
   (setq _x (round __x))
   (setq _y (round __y))
   (setq _intention __intention)
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:intention
   (&optional (__intention :null))
   (if (not (eq __intention :null)) (setq _intention __intention)) _intention)
  (:serialization-length
   ()
   (+
    ;; int32 _x
    4
    ;; int32 _y
    4
    ;; bool _intention
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _x
       (write-long _x s)
     ;; int32 _y
       (write-long _y s)
     ;; bool _intention
       (if _intention (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _x
     (setq _x (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _y
     (setq _y (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; bool _intention
     (setq _intention (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get intention_application::Array :md5sum-) "d6d4ea0cfc5344e240c5b9bd523fcbef")
(setf (get intention_application::Array :datatype-) "intention_application/Array")
(setf (get intention_application::Array :definition-)
      "int32 x
int32 y
bool intention
")



(provide :intention_application/Array "d6d4ea0cfc5344e240c5b9bd523fcbef")


