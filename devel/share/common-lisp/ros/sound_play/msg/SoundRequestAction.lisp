; Auto-generated. Do not edit!


(cl:in-package sound_play-msg)


;//! \htmlinclude SoundRequestAction.msg.html

(cl:defclass <SoundRequestAction> (roslisp-msg-protocol:ros-message)
  ((action_goal
    :reader action_goal
    :initarg :action_goal
    :type sound_play-msg:SoundRequestActionGoal
    :initform (cl:make-instance 'sound_play-msg:SoundRequestActionGoal))
   (action_result
    :reader action_result
    :initarg :action_result
    :type sound_play-msg:SoundRequestActionResult
    :initform (cl:make-instance 'sound_play-msg:SoundRequestActionResult))
   (action_feedback
    :reader action_feedback
    :initarg :action_feedback
    :type sound_play-msg:SoundRequestActionFeedback
    :initform (cl:make-instance 'sound_play-msg:SoundRequestActionFeedback)))
)

(cl:defclass SoundRequestAction (<SoundRequestAction>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SoundRequestAction>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SoundRequestAction)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sound_play-msg:<SoundRequestAction> is deprecated: use sound_play-msg:SoundRequestAction instead.")))

(cl:ensure-generic-function 'action_goal-val :lambda-list '(m))
(cl:defmethod action_goal-val ((m <SoundRequestAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sound_play-msg:action_goal-val is deprecated.  Use sound_play-msg:action_goal instead.")
  (action_goal m))

(cl:ensure-generic-function 'action_result-val :lambda-list '(m))
(cl:defmethod action_result-val ((m <SoundRequestAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sound_play-msg:action_result-val is deprecated.  Use sound_play-msg:action_result instead.")
  (action_result m))

(cl:ensure-generic-function 'action_feedback-val :lambda-list '(m))
(cl:defmethod action_feedback-val ((m <SoundRequestAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sound_play-msg:action_feedback-val is deprecated.  Use sound_play-msg:action_feedback instead.")
  (action_feedback m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SoundRequestAction>) ostream)
  "Serializes a message object of type '<SoundRequestAction>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_goal) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_result) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_feedback) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SoundRequestAction>) istream)
  "Deserializes a message object of type '<SoundRequestAction>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_goal) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_result) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_feedback) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SoundRequestAction>)))
  "Returns string type for a message object of type '<SoundRequestAction>"
  "sound_play/SoundRequestAction")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SoundRequestAction)))
  "Returns string type for a message object of type 'SoundRequestAction"
  "sound_play/SoundRequestAction")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SoundRequestAction>)))
  "Returns md5sum for a message object of type '<SoundRequestAction>"
  "f990cf5de6a2f8e514e825b2c1f4810b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SoundRequestAction)))
  "Returns md5sum for a message object of type 'SoundRequestAction"
  "f990cf5de6a2f8e514e825b2c1f4810b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SoundRequestAction>)))
  "Returns full string definition for message of type '<SoundRequestAction>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%SoundRequestActionGoal action_goal~%SoundRequestActionResult action_result~%SoundRequestActionFeedback action_feedback~%~%================================================================================~%MSG: sound_play/SoundRequestActionGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%SoundRequestGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: sound_play/SoundRequestGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%SoundRequest sound_request~%~%================================================================================~%MSG: sound_play/SoundRequest~%# IMPORTANT: You should never have to generate this message yourself.~%# Use the sound_play::SoundClient C++ helper or the~%# sound_play.libsoundplay.SoundClient Python helper.~%~%# Sounds~%int8 BACKINGUP = 1~%int8 NEEDS_UNPLUGGING = 2~%int8 NEEDS_PLUGGING = 3~%int8 NEEDS_UNPLUGGING_BADLY = 4~%int8 NEEDS_PLUGGING_BADLY = 5~%~%# Sound identifiers that have special meaning~%int8 ALL = -1 # Only legal with PLAY_STOP~%int8 PLAY_FILE = -2~%int8 SAY = -3~%~%int8 sound # Selects which sound to play (see above)~%~%# Commands~%int8 PLAY_STOP = 0 # Stop this sound from playing~%int8 PLAY_ONCE = 1 # Play the sound once~%int8 PLAY_START = 2 # Play the sound in a loop until a stop request occurs~%~%int8 command # Indicates what to do with the sound~%~%# Volume at which to play the sound, with 0 as mute and 1.0 as 100%.~%float32 volume~%~%string arg # file name or text to say~%string arg2 # other arguments~%~%================================================================================~%MSG: sound_play/SoundRequestActionResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%SoundRequestResult result~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: sound_play/SoundRequestResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%bool playing~%time stamp~%~%================================================================================~%MSG: sound_play/SoundRequestActionFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%SoundRequestFeedback feedback~%~%================================================================================~%MSG: sound_play/SoundRequestFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%bool playing~%time stamp~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SoundRequestAction)))
  "Returns full string definition for message of type 'SoundRequestAction"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%SoundRequestActionGoal action_goal~%SoundRequestActionResult action_result~%SoundRequestActionFeedback action_feedback~%~%================================================================================~%MSG: sound_play/SoundRequestActionGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%SoundRequestGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: sound_play/SoundRequestGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%SoundRequest sound_request~%~%================================================================================~%MSG: sound_play/SoundRequest~%# IMPORTANT: You should never have to generate this message yourself.~%# Use the sound_play::SoundClient C++ helper or the~%# sound_play.libsoundplay.SoundClient Python helper.~%~%# Sounds~%int8 BACKINGUP = 1~%int8 NEEDS_UNPLUGGING = 2~%int8 NEEDS_PLUGGING = 3~%int8 NEEDS_UNPLUGGING_BADLY = 4~%int8 NEEDS_PLUGGING_BADLY = 5~%~%# Sound identifiers that have special meaning~%int8 ALL = -1 # Only legal with PLAY_STOP~%int8 PLAY_FILE = -2~%int8 SAY = -3~%~%int8 sound # Selects which sound to play (see above)~%~%# Commands~%int8 PLAY_STOP = 0 # Stop this sound from playing~%int8 PLAY_ONCE = 1 # Play the sound once~%int8 PLAY_START = 2 # Play the sound in a loop until a stop request occurs~%~%int8 command # Indicates what to do with the sound~%~%# Volume at which to play the sound, with 0 as mute and 1.0 as 100%.~%float32 volume~%~%string arg # file name or text to say~%string arg2 # other arguments~%~%================================================================================~%MSG: sound_play/SoundRequestActionResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%SoundRequestResult result~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: sound_play/SoundRequestResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%bool playing~%time stamp~%~%================================================================================~%MSG: sound_play/SoundRequestActionFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%SoundRequestFeedback feedback~%~%================================================================================~%MSG: sound_play/SoundRequestFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%bool playing~%time stamp~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SoundRequestAction>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_goal))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_result))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_feedback))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SoundRequestAction>))
  "Converts a ROS message object to a list"
  (cl:list 'SoundRequestAction
    (cl:cons ':action_goal (action_goal msg))
    (cl:cons ':action_result (action_result msg))
    (cl:cons ':action_feedback (action_feedback msg))
))
