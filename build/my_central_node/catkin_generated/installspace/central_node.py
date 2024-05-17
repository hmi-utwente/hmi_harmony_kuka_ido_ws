#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Point
import pandas as pd

class CentralNode:
    def __init__(self):
        rospy.init_node('central_node')
        self.dataset = pd.DataFrame(columns=['frame_x', 'frame_y', 'obstacle_check'])
        rospy.Subscriber('frame', Point, self.frame_callback)
        rospy.Subscriber('obstacle_check', String, self.obstacle_check_callback)

    def frame_callback(self, data):
        # Store the latest frame data as a data point in the dataset
        new_data = {'frame_x': data.x, 'frame_y': data.y, 'obstacle_check': None}
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
