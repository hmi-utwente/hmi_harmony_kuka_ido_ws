##!/usr/bin/env python

#import rospy
#import numpy as np
#import math
#from geometry_msgs.msg import Twist
#from sensor_msgs.msg import LaserScan
#from ros_openpose.msg import Frame
#from robot_movement.robot_movement_script import RobotMovement as robot_movement
#import time

# Global variables to keep track of the state
#object_detected = False
#person_detected = False
#obstruction_resolved = False
#persons_in_proximity = False
#
#def frame_callback(frame_msg):
#    global person_detected
#    if not frame_msg.persons:
#        rospy.logwarn("No person detected!")
#        person_detected = False
#    else:
#        rospy.logwarn("Person detected!")
#        person_detected = True

#def point_towards_obstruction(scan_msg,valid_ranges):
#    if valid_ranges:
#        if all(val > 0.8 for val in valid_ranges):
#            object_detected = False
#            rospy.loginfo("No blockage of the way")
#        else:
        # Find the minimum range value and its index
#            min_range = min(valid_ranges)
#            min_range_index = scan_msg.ranges.index(min_range)

        # Calculate the angle corresponding to the minimum range index
#            angle_increment = scan_msg.angle_increment
#            angle_min = scan_msg.angle_min 
#            angle_at_min_range = (angle_min + min_range_index * angle_increment) 

        # Calculate the turning angle relative to the robot's orientation
#            turning_angle =  angle_at_min_range  # Subtracting pi/2 to face the object directly
            #turning_angle = angle_at_min_range
#            rospy.loginfo(turning_angle)
#            idx = 0
#            while person_detected == False:
#                robot_movement().rotate(turning_angle + math.pi,127)
#                time.sleep(5)
#                idx += 1
#                if idx == 4:
#                    rospy.loginfo("Turned 360 degrees, no person detected")
#                    break
#            else:
#                rospy.loginfo("Obstacle in the way, can you help?")
                

#def scan_callback(scan_msg):
#    global object_detected, obstruction_resolved, persons_in_proximity

    # Check if there are any valid range values in the laser scan
#    valid_ranges = [range_val for range_val in scan_msg.ranges if not np.isnan(range_val)]

    # Check if there are obstacles in the scan data
#    if valid_ranges:
#        object_detected = True
#    else:
#        object_detected = False

    # Check conditions and react accordingly
#    if object_detected:
#        rospy.loginfo("Object detected")
#        point_towards_obstruction(scan_msg,valid_ranges)
#    else:
#        rospy.loginfo("No object detected")

#def person_detector():
#    rospy.init_node('person_detector', anonymous=True)
#    rospy.Subscriber('/frame', Frame, frame_callback)
#    rospy.Subscriber('/scan_obstacles', LaserScan, scan_callback)
#    rospy.spin()

#if __name__ == '__main__':
#    try:
#        person_detector()
#    except rospy.ROSInterruptException:
#        pass

#!/usr/bin/env python

import rospy
import numpy as np
import math
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from ros_openpose.msg import Frame
from robot_movement.robot_movement_script import RobotMovement as robot_movement
import time

class Behaviors:
    def __init__(self):
        self.object_detected = False
        self.person_detected = False
        self.obstruction_resolved = False
        self.persons_in_proximity = False

        rospy.init_node('person_detector', anonymous=True)
        rospy.Subscriber('/frame', Frame, self.frame_callback)
        rospy.Subscriber('/scan_obstacles', LaserScan, self.scan_callback)

    def frame_callback(self, frame_msg):
        if not frame_msg.persons:
            rospy.logwarn("No person detected!")
            self.person_detected = False
        else:
            rospy.logwarn("Person detected!")
            self.person_detected = True

    def point_towards_obstruction(self, scan_msg, valid_ranges):
        if valid_ranges:
            if all(val > 0.6 for val in valid_ranges):
                self.object_detected = False
                rospy.loginfo("No blockage of the way")
            else:
                min_range = min(valid_ranges)
                min_range_index = scan_msg.ranges.index(min_range)
                angle_increment = scan_msg.angle_increment
                angle_min = scan_msg.angle_min 
                angle_at_min_range = (angle_min + min_range_index * angle_increment) 
                turning_angle = angle_at_min_range
                rospy.loginfo(turning_angle)
                idx = 0
                while not self.person_detected:
                    robot_movement().rotate(turning_angle + math.pi, 127)
                    time.sleep(5)
                    idx += 1
                    if idx == 4:
                        rospy.loginfo("Turned 360 degrees, no person detected")
                        break
                else:
                    rospy.loginfo("Obstacle in the way, can you help?")

    def scan_callback(self, scan_msg):
        valid_ranges = [range_val for range_val in scan_msg.ranges if not np.isnan(range_val)]
        if valid_ranges:
            self.object_detected = True
        else:
            self.object_detected = False

        if self.object_detected:
            rospy.loginfo("Object detected")
            self.point_towards_obstruction(scan_msg, valid_ranges)
        else:
            rospy.loginfo("No object detected")

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        pd = Behaviors()
        pd.run()
    except rospy.ROSInterruptException:
        pass
