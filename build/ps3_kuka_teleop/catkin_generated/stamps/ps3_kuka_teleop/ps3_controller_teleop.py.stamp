#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

# Initialize linear and angular velocities
linear_vel = 0.0
angular_vel = 0.0

# Define scaling factors for velocity adjustment
linear_scale = 1.5
angular_scale = 127.5

def joy_callback(msg):
    global linear_vel, angular_vel

    # Map joystick axes to linear and angular velocities
    linear_vel = msg.axes[1] * linear_scale   # Left stick vertical axis
    angular_vel = msg.axes[3] * angular_scale  # Right stick horizontal axis

def publish_command():
    # Create Twist message
    twist = Twist()
    twist.linear.x = linear_vel
    twist.angular.z = angular_vel

    # Publish Twist message
    pub.publish(twist)

if __name__ == "__main__":
    rospy.init_node("ps3_controller_teleop")

    # Initialize publisher for Twist messages
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=50)

    # Subscribe to Joy messages from the joystick
    rospy.Subscriber("/joy", Joy, joy_callback)

    rate = rospy.Rate(100)  # Adjust the rate (e.g., 10 Hz) as needed

    # Main loop
    while not rospy.is_shutdown():
        # Continuously publish Twist messages based on the last command received
        publish_command()
        rate.sleep()
