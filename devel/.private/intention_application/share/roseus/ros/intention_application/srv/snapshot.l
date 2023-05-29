;; Auto-generated. Do not edit!


(when (boundp 'intention_application::snapshot)
  (if (not (find-package "INTENTION_APPLICATION"))
    (make-package "INTENTION_APPLICATION"))
  (shadow 'snapshot (find-package "INTENTION_APPLICATION")))
(unless (find-package "INTENTION_APPLICATION::SNAPSHOT")
  (make-package "INTENTION_APPLICATION::SNAPSHOT"))
(unless (find-package "INTENTION_APPLICATION::SNAPSHOTREQUEST")
  (make-package "INTENTION_APPLICATION::SNAPSHOTREQUEST"))
(unless (find-package "INTENTION_APPLICATION::SNAPSHOTRESPONSE")
  (make-package "INTENTION_APPLICATION::SNAPSHOTRESPONSE"))

(in-package "ROS")





(defclass intention_application::snapshotRequest
  :super ros::object
  :slots ())

(defmethod intention_application::snapshotRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass intention_application::snapshotResponse
  :super ros::object
  :slots (_data ))

(defmethod intention_application::snapshotResponse
  (:init
   (&key
    ((:data __data) nil)
    )
   (send-super :init)
   (setq _data __data)
   self)
  (:data
   (&optional (__data :null))
   (if (not (eq __data :null)) (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; bool _data
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _data
       (if _data (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _data
     (setq _data (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass intention_application::snapshot
  :super ros::object
  :slots ())

(setf (get intention_application::snapshot :md5sum-) "8b94c1b53db61fb6aed406028ad6332a")
(setf (get intention_application::snapshot :datatype-) "intention_application/snapshot")
(setf (get intention_application::snapshot :request) intention_application::snapshotRequest)
(setf (get intention_application::snapshot :response) intention_application::snapshotResponse)

(defmethod intention_application::snapshotRequest
  (:response () (instance intention_application::snapshotResponse :init)))

(setf (get intention_application::snapshotRequest :md5sum-) "8b94c1b53db61fb6aed406028ad6332a")
(setf (get intention_application::snapshotRequest :datatype-) "intention_application/snapshotRequest")
(setf (get intention_application::snapshotRequest :definition-)
      "---
bool data

")

(setf (get intention_application::snapshotResponse :md5sum-) "8b94c1b53db61fb6aed406028ad6332a")
(setf (get intention_application::snapshotResponse :datatype-) "intention_application/snapshotResponse")
(setf (get intention_application::snapshotResponse :definition-)
      "---
bool data

")



(provide :intention_application/snapshot "8b94c1b53db61fb6aed406028ad6332a")


