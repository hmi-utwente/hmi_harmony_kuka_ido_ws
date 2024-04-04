#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from ros_openpose.msg import Frame
from robot_movement.robot_movement_script import RobotMovement as robot_movement
import time
def frame_callback(msg_persons):
    if not msg_persons.persons:
        rospy.logwarn("No person detected!")
        robot_movement().rotate(1,1)
        time.sleep(10)
    else:
        rospy.logwarn("Person detected!")
        robot_movement().move(2,1)
        time.sleep(5)


def person_detector():
    rospy.init_node('person_detector', anonymous=True)
    rospy.Subscriber('/frame', Frame, frame_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        person_detector()
    except rospy.ROSInterruptException:
        pass


