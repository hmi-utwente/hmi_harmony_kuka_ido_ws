#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

from my_robot_scan.scan_listener_script import Behaviors
# Initialize linear and angular velocities
linear_vel = 0.0
angular_vel = 0.0

# Define scaling factors for velocity adjustment
linear_scale = 0.65 
angular_scale = 127
behaviors_instance = None

def joy_callback(msg):
    global linear_vel, angular_vel, behaviors_instance
    status_obstacle = 0
    # Map joystick axes to linear and angular velocities
    linear_vel = msg.axes[1] * linear_scale   # Left stick vertical axis
    angular_vel = msg.axes[3] * angular_scale  # Right stick horizontal axis
    
    #Configuration for behaviours (xbox controller based):
    if msg.buttons[0]:  # A button
        rospy.loginfo("A button pressed")
        if behaviors_instance is not None:
            behaviors_instance.stop_rotation= True
            behaviors_instance.button_press_a = True
            behaviors_instance.button_press_y = False
            behaviors_instance.button_press_x = False
            behaviors_instance.button_press_b = False
        else:
            stop_rotate= True
            button_press_a = True
            button_press_y = False
            button_press_x = False
            button_press_b = False
            behaviors_instance = Behaviors(stop_rotate, button_press_y,button_press_x, button_press_b, button_press_a) 
            

    elif msg.buttons[1]:  # B button
        rospy.loginfo("B button pressed")
        if behaviors_instance is not None:
            behaviors_instance.stop_rotate= True
            behaviors_instance.button_press_a = False
            behaviors_instance.button_press_y = False
            behaviors_instance.button_press_x = False
            behaviors_instance.button_press_b = True
        else:
            stop_rotate = True
            button_press_a = False
            button_press_x = False
            button_press_b = True
            button_press_y = False
            behaviors_instance = Behaviors(stop_rotate, button_press_y,button_press_x, button_press_b, button_press_a) 
            #behaviors_instance.obstacle()

    elif msg.buttons[2]:  # X button
        rospy.loginfo("X button pressed")
        if behaviors_instance is not None:
            behaviors_instance.stop_rotation= True
            behaviors_instance.button_press_a = False
            behaviors_instance.button_press_y = False
            behaviors_instance.button_press_x = True
            behaviors_instance.button_press_b = False
        else:
            stop_rotate = True
            button_press_a = False
            button_press_x = True
            button_press_b = False
            button_press_y = False
            behaviors_instance = Behaviors(stop_rotate, button_press_y,button_press_x, button_press_b, button_press_a) 
            #behaviors_instance.mobility()
    elif msg.buttons[3]:  # Y button
        #block the way
        rospy.loginfo("Y button pressed")
        if behaviors_instance is not None:
            behaviors_instance.stop_rotate = False
            behaviors_instance.button_press_a = False
            behaviors_instance.button_press_x = False
            behaviors_instance.button_press_b = False
            behaviors_instance.button_press_y = True
        else:
            stop_rotate = False
            button_press_a = False
            button_press_x = False
            button_press_b = False
            button_press_y = True
            behaviors_instance = Behaviors(stop_rotate, button_press_y,button_press_x, button_press_b, button_press_a) 
            behaviors_instance.obstacle()

def publish_command():
    # Create Twist message
    twist = Twist()
    twist.linear.x = linear_vel
    twist.angular.z = angular_vel

    # Publish Twist message
    pub.publish(twist)

if __name__ == "__main__":
    rospy.init_node("ps3_controller_teleop", anonymous=True)

    # Initialize publisher for Twist messages
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    # Subscribe to Joy messages from the joystick
    rospy.Subscriber("/joy", Joy, joy_callback)

    rate = rospy.Rate(100)  # Adjust the rate (e.g., 10 Hz) as needed

    # Main loop
    while not rospy.is_shutdown():
        # Continuously publish Twist messages based on the last command received
        publish_command()
        rate.sleep()
