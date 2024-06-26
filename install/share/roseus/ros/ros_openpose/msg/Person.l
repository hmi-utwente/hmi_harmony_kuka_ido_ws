;; Auto-generated. Do not edit!


(when (boundp 'ros_openpose::Person)
  (if (not (find-package "ROS_OPENPOSE"))
    (make-package "ROS_OPENPOSE"))
  (shadow 'Person (find-package "ROS_OPENPOSE")))
(unless (find-package "ROS_OPENPOSE::PERSON")
  (make-package "ROS_OPENPOSE::PERSON"))

(in-package "ROS")
;;//! \htmlinclude Person.msg.html


(defclass ros_openpose::Person
  :super ros::object
  :slots (_bodyParts _leftHandParts _rightHandParts _faceParts ))

(defmethod ros_openpose::Person
  (:init
   (&key
    ((:bodyParts __bodyParts) ())
    ((:leftHandParts __leftHandParts) ())
    ((:rightHandParts __rightHandParts) ())
    ((:faceParts __faceParts) ())
    )
   (send-super :init)
   (setq _bodyParts __bodyParts)
   (setq _leftHandParts __leftHandParts)
   (setq _rightHandParts __rightHandParts)
   (setq _faceParts __faceParts)
   self)
  (:bodyParts
   (&rest __bodyParts)
   (if (keywordp (car __bodyParts))
       (send* _bodyParts __bodyParts)
     (progn
       (if __bodyParts (setq _bodyParts (car __bodyParts)))
       _bodyParts)))
  (:leftHandParts
   (&rest __leftHandParts)
   (if (keywordp (car __leftHandParts))
       (send* _leftHandParts __leftHandParts)
     (progn
       (if __leftHandParts (setq _leftHandParts (car __leftHandParts)))
       _leftHandParts)))
  (:rightHandParts
   (&rest __rightHandParts)
   (if (keywordp (car __rightHandParts))
       (send* _rightHandParts __rightHandParts)
     (progn
       (if __rightHandParts (setq _rightHandParts (car __rightHandParts)))
       _rightHandParts)))
  (:faceParts
   (&rest __faceParts)
   (if (keywordp (car __faceParts))
       (send* _faceParts __faceParts)
     (progn
       (if __faceParts (setq _faceParts (car __faceParts)))
       _faceParts)))
  (:serialization-length
   ()
   (+
    ;; ros_openpose/BodyPart[] _bodyParts
    (apply #'+ (send-all _bodyParts :serialization-length)) 4
    ;; ros_openpose/BodyPart[] _leftHandParts
    (apply #'+ (send-all _leftHandParts :serialization-length)) 4
    ;; ros_openpose/BodyPart[] _rightHandParts
    (apply #'+ (send-all _rightHandParts :serialization-length)) 4
    ;; ros_openpose/BodyPart[] _faceParts
    (apply #'+ (send-all _faceParts :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; ros_openpose/BodyPart[] _bodyParts
     (write-long (length _bodyParts) s)
     (dolist (elem _bodyParts)
       (send elem :serialize s)
       )
     ;; ros_openpose/BodyPart[] _leftHandParts
     (write-long (length _leftHandParts) s)
     (dolist (elem _leftHandParts)
       (send elem :serialize s)
       )
     ;; ros_openpose/BodyPart[] _rightHandParts
     (write-long (length _rightHandParts) s)
     (dolist (elem _rightHandParts)
       (send elem :serialize s)
       )
     ;; ros_openpose/BodyPart[] _faceParts
     (write-long (length _faceParts) s)
     (dolist (elem _faceParts)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; ros_openpose/BodyPart[] _bodyParts
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _bodyParts (let (r) (dotimes (i n) (push (instance ros_openpose::BodyPart :init) r)) r))
     (dolist (elem- _bodyParts)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; ros_openpose/BodyPart[] _leftHandParts
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _leftHandParts (let (r) (dotimes (i n) (push (instance ros_openpose::BodyPart :init) r)) r))
     (dolist (elem- _leftHandParts)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; ros_openpose/BodyPart[] _rightHandParts
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _rightHandParts (let (r) (dotimes (i n) (push (instance ros_openpose::BodyPart :init) r)) r))
     (dolist (elem- _rightHandParts)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; ros_openpose/BodyPart[] _faceParts
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _faceParts (let (r) (dotimes (i n) (push (instance ros_openpose::BodyPart :init) r)) r))
     (dolist (elem- _faceParts)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get ros_openpose::Person :md5sum-) "719781611105baee252c1ac007e97ed7")
(setf (get ros_openpose::Person :datatype-) "ros_openpose/Person")
(setf (get ros_openpose::Person :definition-)
      "# A person has some body parts. That is why we have created
# an array of body parts.
BodyPart[] bodyParts
BodyPart[] leftHandParts
BodyPart[] rightHandParts
BodyPart[] faceParts

================================================================================
MSG: ros_openpose/BodyPart
# The location and score of body parts are stored in a float array.
# Therefore we are using 32 bits instead of 64 bits.
# src: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/include/openpose/core/datum.hpp
float32 score
Pixel pixel
geometry_msgs/Point32 point

================================================================================
MSG: ros_openpose/Pixel
# The location and score of body parts are stored in a float array.
# Therefore we are using 32 bits instead of 64 bits.
# src: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/include/openpose/core/datum.hpp
# The location has been resized to the desired output
# resolution (e.g., `resolution` flag in the demo).
float32 x
float32 y

================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z
")



(provide :ros_openpose/Person "719781611105baee252c1ac007e97ed7")


