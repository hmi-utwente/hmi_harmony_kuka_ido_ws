#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from playsound import playsound

def sound_callback(msg):
    if msg.data == "request_assistance":
        rospy.loginfo("Playing sound")
        # Replace 'path_to_sound_file' with the path to your sound file
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/request-for-assistance.wav')
    if msg.data == "oh_surprised_block":
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/oh-surprise-blocked.wav')

    if msg.data =='draw_attention':
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/draw-attention.wav')

    if msg.data == 'blocked_multiple_attempts':
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/blocked-multiple-attempts.wav')

    if msg.data == "hello":
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/hello.wav')
    
    if msg.data == "happy":
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/happy.wav')
    
    if msg.data == "Do you need assistance?":
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/do-you-need-help.wav')

    if msg.data == "request assistance":
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/request-for-assistance.wav')

    if msg.data == "thankyou-bye":
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/request-for-assistance.wav')

    if msg.data == "takecare":
        playsound('/home/arjan/Desktop/ros_noetic_base_2204/for-kuka/take-care2.wav')






def sound_player():
    rospy.init_node('sound_player', anonymous=True)
    rospy.Subscriber('/sound_command', String, sound_callback)
    rospy.spin()

if __name__ == '__main__':
    sound_player()
