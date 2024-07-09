#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from playsound import playsound

def sound_callback(msg):
    if msg.data == "request_assistance" or msg.data == 'other1':
        rospy.loginfo("Playing sound")
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/request-for-assistance.wav')
    elif msg.data == "oh_surprised_block" or msg.data == 'other2':
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/oh-surprise-blocked.wav')
    elif msg.data == 'draw_attention' or msg.data == 'other3':
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/draw-attention.wav')
    elif msg.data == 'blocked_multiple_attempts' or msg.data == 'other4':
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/request-for-assistance.wav')
    elif msg.data == "hello" or msg.data == 'positive1':
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/hello.wav')
    elif msg.data == "happy" or msg.data == 'positive2':
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/happy2.wav')
    elif msg.data == "Do you need assistance?" or msg.data == 'positive3':
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/do-you-need-help.wav')
    elif msg.data == "oeps" or msg.data == 'other5':
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/oops-surprise-blocked.wav')
    elif msg.data == "thankyou-bye":
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/request-for-assistance.wav')
    elif msg.data == "takecare":
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/take-care3.wav')
    else:
        rospy.logwarn(f"Unknown command received: {msg.data}")

def sound_player():
    rospy.init_node('sound_player', anonymous=True)
    rospy.Subscriber('/sound_command', String, sound_callback)
    rospy.spin()

if __name__ == '__main__':
    sound_player()

