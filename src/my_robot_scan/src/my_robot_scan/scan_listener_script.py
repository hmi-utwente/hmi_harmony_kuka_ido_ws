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


#Parameters
close_range = 0.7
speed = 127


class Behaviors:
    def __init__(self,stop_rotate):
        self.object_detected = False
        self.person_detected = False
        self.object_detected_close_range = False
        self.obstruction_resolved = False
        self.persons_in_proximity = False
        self.latest_scan_msg = None

        #rospy.init_node('person_detector', anonymous=True)
        rospy.Subscriber('/frame', Frame, self.frame_callback)
        rospy.Subscriber('/scan_obstacles', LaserScan, self.scan_callback)

        self.stop_rotation = stop_rotate 

    
    def frame_callback(self, frame_msg):
        if not frame_msg.persons:
            rospy.logwarn("No person detected!")
            self.person_detected = False
        else:
            rospy.logwarn("Person detected!")
            self.person_detected = True

    def point_towards_obstruction(self):

        while self.object_detected and not self.stop_rotation:
            
            if self.latest_scan_msg:
                valid_ranges = [range_val for range_val in self.latest_scan_msg.ranges if not np.isnan(range_val)]
                if valid_ranges:
                    if all(val > close_range for val in valid_ranges):
                        rospy.loginfo(valid_ranges)
                        self.object_detected = False
                        rospy.loginfo("No obstruction of the way")
                        self.stop_rotation = True
                        return
                    else:
                        min_range = min(valid_ranges)
                        min_range_index = self.latest_scan_msg.ranges.index(min_range)
                        angle_increment = self.latest_scan_msg.angle_increment
                        angle_min = self.latest_scan_msg.angle_min 
                        angle_at_min_range = angle_min + min_range_index * angle_increment
                        turning_angle = angle_at_min_range
                        rospy.loginfo(turning_angle)
                        idx = 0
                        if not self.person_detected and not self.stop_rotation:
                            idx = 0
                            while idx  <= 3: #rotate 360 degrees in steps
                                robot_movement().rotate(0.5 * math.pi, speed)
                                rospy.loginfo("Check for people...")
                                time.sleep(15)
                                idx += 1
                                if self.person_detected:
                                    rospy.loginfo("Person detected, can you help me")
                                else:
                                    rospy.loginfo("Rotation: " + idx +" ,no person detected")
                            self.stop_rotation = True
                            return
                        else:
                            rospy.loginfo("Obstacle in the way, can you help?")
                            return
                else:
                    rospy.loginfo("No valid ranges in laser scan data")
                    return
            else:
                rospy.loginfo("No laser scan data received")
                return


    def scan_callback(self, scan_msg):
        self.latest_scan_msg = scan_msg
        valid_ranges = [range_val for range_val in scan_msg.ranges if not np.isnan(range_val)]
        if valid_ranges:
            if any(val < close_range for val in valid_ranges):
                self.object_detected_close_range = True
            self.object_detected = True
        else:
            self.object_detected = False

        if self.object_detected:
            #rospy.loginfo("Object detected")
            if not self.stop_rotation:
                self.point_towards_obstruction()
            else:
                rospy.loginfo("Signaling for help, obstacle in the way")
        else:
            rospy.loginfo("No object detected")

    def run(self):
        rospy.spin()

#if __name__ == '__main__':
#    try:
#        pd = Behaviors()
#        pd.run()
#    except rospy.ROSInterruptException:
#        pass
