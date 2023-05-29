; Auto-generated. Do not edit!


(cl:in-package intention_application-srv)


;//! \htmlinclude snapshot-request.msg.html

(cl:defclass <snapshot-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass snapshot-request (<snapshot-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <snapshot-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'snapshot-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name intention_application-srv:<snapshot-request> is deprecated: use intention_application-srv:snapshot-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <snapshot-request>) ostream)
  "Serializes a message object of type '<snapshot-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <snapshot-request>) istream)
  "Deserializes a message object of type '<snapshot-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<snapshot-request>)))
  "Returns string type for a service object of type '<snapshot-request>"
  "intention_application/snapshotRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'snapshot-request)))
  "Returns string type for a service object of type 'snapshot-request"
  "intention_application/snapshotRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<snapshot-request>)))
  "Returns md5sum for a message object of type '<snapshot-request>"
  "8b94c1b53db61fb6aed406028ad6332a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'snapshot-request)))
  "Returns md5sum for a message object of type 'snapshot-request"
  "8b94c1b53db61fb6aed406028ad6332a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<snapshot-request>)))
  "Returns full string definition for message of type '<snapshot-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'snapshot-request)))
  "Returns full string definition for message of type 'snapshot-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <snapshot-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <snapshot-request>))
  "Converts a ROS message object to a list"
  (cl:list 'snapshot-request
))
;//! \htmlinclude snapshot-response.msg.html

(cl:defclass <snapshot-response> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass snapshot-response (<snapshot-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <snapshot-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'snapshot-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name intention_application-srv:<snapshot-response> is deprecated: use intention_application-srv:snapshot-response instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <snapshot-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader intention_application-srv:data-val is deprecated.  Use intention_application-srv:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <snapshot-response>) ostream)
  "Serializes a message object of type '<snapshot-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'data) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <snapshot-response>) istream)
  "Deserializes a message object of type '<snapshot-response>"
    (cl:setf (cl:slot-value msg 'data) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<snapshot-response>)))
  "Returns string type for a service object of type '<snapshot-response>"
  "intention_application/snapshotResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'snapshot-response)))
  "Returns string type for a service object of type 'snapshot-response"
  "intention_application/snapshotResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<snapshot-response>)))
  "Returns md5sum for a message object of type '<snapshot-response>"
  "8b94c1b53db61fb6aed406028ad6332a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'snapshot-response)))
  "Returns md5sum for a message object of type 'snapshot-response"
  "8b94c1b53db61fb6aed406028ad6332a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<snapshot-response>)))
  "Returns full string definition for message of type '<snapshot-response>"
  (cl:format cl:nil "bool data~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'snapshot-response)))
  "Returns full string definition for message of type 'snapshot-response"
  (cl:format cl:nil "bool data~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <snapshot-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <snapshot-response>))
  "Converts a ROS message object to a list"
  (cl:list 'snapshot-response
    (cl:cons ':data (data msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'snapshot)))
  'snapshot-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'snapshot)))
  'snapshot-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'snapshot)))
  "Returns string type for a service object of type '<snapshot>"
  "intention_application/snapshot")