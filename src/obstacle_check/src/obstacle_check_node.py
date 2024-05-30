#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
import math

def laser_callback(scan):
    # Safety threshold distance in meters
    threshold_distance = 1.5

    # Calculate the index corresponding to the angle 0 radians (straight ahead)
    center_index = int((0.0 - scan.angle_min) / scan.angle_increment)

    # Define a window around the center to check for obstacles
    window_size = 10  # number of indices to check around the center
    start_index = max(0, center_index - window_size)
    end_index = min(len(scan.ranges), center_index + window_size)

    # Check if any of the range measurements within the window are less than the threshold
    obstacle_detected = False
    for i in range(start_index, end_index + 1):
        distance = scan.ranges[i]
        if not math.isnan(distance) and distance < threshold_distance:
            obstacle_detected = True
            break

    # Publish the result
    msg = String()
    if obstacle_detected:
        msg.data = "Path is blocked. Obstacle detected."
    else:
        msg.data = "Path is clear. Safe to move forward."
    obstacle_pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node('obstacle_check_node')
    laser_sub = rospy.Subscriber('/scan_slam', LaserScan, laser_callback)
    obstacle_pub = rospy.Publisher('obstacle_check', String, queue_size=10)
    rospy.spin()
