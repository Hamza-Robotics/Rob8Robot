; Auto-generated. Do not edit!


(cl:in-package intention_application-msg)


;//! \htmlinclude Array.msg.html

(cl:defclass <Array> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:integer
    :initform 0)
   (y
    :reader y
    :initarg :y
    :type cl:integer
    :initform 0)
   (intention
    :reader intention
    :initarg :intention
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Array (<Array>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Array>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Array)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name intention_application-msg:<Array> is deprecated: use intention_application-msg:Array instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <Array>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader intention_application-msg:x-val is deprecated.  Use intention_application-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <Array>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader intention_application-msg:y-val is deprecated.  Use intention_application-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'intention-val :lambda-list '(m))
(cl:defmethod intention-val ((m <Array>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader intention_application-msg:intention-val is deprecated.  Use intention_application-msg:intention instead.")
  (intention m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Array>) ostream)
  "Serializes a message object of type '<Array>"
  (cl:let* ((signed (cl:slot-value msg 'x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'intention) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Array>) istream)
  "Deserializes a message object of type '<Array>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'y) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:setf (cl:slot-value msg 'intention) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Array>)))
  "Returns string type for a message object of type '<Array>"
  "intention_application/Array")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Array)))
  "Returns string type for a message object of type 'Array"
  "intention_application/Array")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Array>)))
  "Returns md5sum for a message object of type '<Array>"
  "d6d4ea0cfc5344e240c5b9bd523fcbef")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Array)))
  "Returns md5sum for a message object of type 'Array"
  "d6d4ea0cfc5344e240c5b9bd523fcbef")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Array>)))
  "Returns full string definition for message of type '<Array>"
  (cl:format cl:nil "int32 x~%int32 y~%bool intention~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Array)))
  "Returns full string definition for message of type 'Array"
  (cl:format cl:nil "int32 x~%int32 y~%bool intention~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Array>))
  (cl:+ 0
     4
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Array>))
  "Converts a ROS message object to a list"
  (cl:list 'Array
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':intention (intention msg))
))
