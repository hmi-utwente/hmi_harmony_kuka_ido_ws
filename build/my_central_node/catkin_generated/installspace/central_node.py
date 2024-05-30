#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Point
from ros_openpose.msg import Frame
import pandas as pd

class CentralNode:
    def __init__(self):
        rospy.init_node('central_node')
        self.dataset = pd.DataFrame(columns=['obstacle_check', 'persons'])
        rospy.Subscriber('frame', Frame, self.frame_callback)  # Replace YourFrameMessageType with the actual message type
        rospy.Subscriber('obstacle_check', String, self.obstacle_check_callback)

    def frame_callback(self, data):
        # Extract relevant information from the frame data and store it in the dataset
        persons_data = []
        for person in data.persons:
            body_parts = []
            for body_part in person.bodyParts:
                body_parts.append({
                    'score': body_part.score,
                    'pixel_x': body_part.pixel.x,
                    'pixel_y': body_part.pixel.y,
                    'point_z': body_part.point.z
                })
            persons_data.append({'bodyParts': body_parts})
        
        new_data = {'persons': persons_data}
        self.dataset = self.dataset.append(new_data, ignore_index=True)

    def obstacle_check_callback(self, data):
        # Update the latest obstacle check result in the dataset
        if not self.dataset.empty:
            self.dataset.at[self.dataset.index[-1], 'obstacle_check'] = data.data
        
    
    def print_dataset(self):
        # Print the current dataset
        rospy.loginfo("\n{}".format(self.dataset))

if __name__ == '__main__':
    try:
        central_node = CentralNode()
        rate = rospy.Rate(1)  # 1 Hz
        while not rospy.is_shutdown():
            central_node.print_dataset()
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
