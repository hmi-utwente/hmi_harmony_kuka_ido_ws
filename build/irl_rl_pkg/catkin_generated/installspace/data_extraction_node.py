#!/usr/bin/env python3
import rospy
import rosbag
import pandas as pd
from ros_openpose.msg import Frame  # Replace with the actual package and message type
from std_msgs.msg import String
from math import floor

class DataExtractionNode:
    def __init__(self):
        rospy.init_node('data_extraction_node')
        self.dataset_openpose = pd.DataFrame(columns=['timestamp', 'person_id', 'body_part_id', 'pixel_x', 'pixel_y', 'point_z', 'score'])
        self.dataset_obstacle_check = pd.DataFrame(columns=['timestamp', 'blocked_path'])
        self.dataset_sound = pd.DataFrame(columns=['timestamp', 'sound'])
        self.merged_data = None
        self.bag_files = [
        "/home/arjan/Desktop/data/data_processed/p11.bag",
        "/home/arjan/Desktop/data/data_processed/p12.bag",
        "/home/arjan/Desktop/data/data_processed/p13.bag",
        "/home/arjan/Desktop/data/data_processed/p31.bag",
        "/home/arjan/Desktop/data/data_processed/p32.bag",
        "/home/arjan/Desktop/data/data_processed/p33.bag",
        "/home/arjan/Desktop/data/data_processed/p41.bag",
        "/home/arjan/Desktop/data/data_processed/p42.bag",
        "/home/arjan/Desktop/data/data_processed/p43.bag",
        "/home/arjan/Desktop/data/data_processed/p51.bag",
        "/home/arjan/Desktop/data/data_processed/p52.bag",
        "/home/arjan/Desktop/data/data_processed/p53.bag",
        "/home/arjan/Desktop/data/data_processed/p61.bag",
        "/home/arjan/Desktop/data/data_processed/p62.bag",
        "/home/arjan/Desktop/data/data_processed/p63.bag",
        "/home/arjan/Desktop/data/data_processed/p71.bag",
        "/home/arjan/Desktop/data/data_processed/p81.bag",
        "/home/arjan/Desktop/data/data_processed/p82.bag",
        "/home/arjan/Desktop/data/data_processed/p83.bag"
        ]
       
        self.bag_files = rospy.get_param('~bag_files', self.bag_files) 
        self.extract_data_from_bags()
        
    def extract_data_from_bags(self):
        for bag_file in self.bag_files:
            rospy.loginfo(f"Processing bag file: {bag_file}")
            bag = rosbag.Bag(bag_file)
            for topic, msg, t in bag.read_messages():
                if topic == '/frame':  # Adjust to match your topic name
                    self.frame_callback(msg,t)
                if topic == 'obstacle_check':  # Adjust to match your topic name
                    self.obstacle_check_callback(msg,t)

                if topic == '/sound_command':
                    self.sound_callback(msg,t)
            bag.close()
        
        self.dataset_openpose['timestamp'] = self.dataset_openpose['timestamp'].apply(lambda x: floor(x))
        self.dataset_obstacle_check['timestamp'] = self.dataset_obstacle_check['timestamp'].apply(lambda x: floor(x))
        self.dataset_sound['timestamp'] = self.dataset_sound['timestamp'].apply(lambda x: floor(x))
        # Set the DataFrame as a ROS parameter (could also save to a file if too large)
        rospy.set_param('extracted_data_openpose', self.dataset_openpose.to_dict(orient='list'))
        rospy.set_param('extracted_obstacle_check', self.dataset_obstacle_check.to_dict(orient='list'))
        rospy.set_param('extracted_sound', self.dataset_sound.to_dict(orient='list'))
        self.merged_dataset = pd.merge(self.dataset_openpose, self.dataset_obstacle_check, on='timestamp')
        self.merged_dataset = pd.merge(self.merged_dataset, self.dataset_sound, on='timestamp', how='left' )
        self.merged_dataset['sound'].fillna('no_sound', inplace=True)

        rows_per_file = 500000  # Adjust this value based on your requirements

        # Splitting the DataFrame into multiple CSV files
        for i in range(0, len(self.merged_dataset), rows_per_file):
            part = self.merged_dataset.iloc[i:i + rows_per_file]
            part.to_csv(f'/home/arjan/Desktop/large_dataset_part_{i//rows_per_file + 1}.csv', index=False)

        rospy.set_param("merged_data", self.merged_dataset.to_dict(orient='list'))
        rospy.loginfo("Data extraction complete and parameter set.")

    def frame_callback(self, data, timestamp):
        # Extract relevant information from the frame data and store it in the dataset
        for person_id, person in enumerate(data.persons):
            for body_part_id, body_part in enumerate(person.bodyParts):
                new_data = {
                    'timestamp': timestamp.to_sec(),
                    'person_id': person_id,
                    'body_part_id': body_part_id,
                    'pixel_x': body_part.pixel.x,
                    'pixel_y': body_part.pixel.y,
                    'point_z': body_part.point.z,
                    'score': body_part.score
                }
                self.dataset_openpose = self.dataset_openpose.append(new_data, ignore_index=True)
                self.dataset_openpose = self.dataset_openpose.dropna()
                rospy.loginfo(f"New data appended: {new_data}")
        
    def obstacle_check_callback(self, data,timestamp):
        # Update the current obstacle check state
        new_data = {
            'timestamp': timestamp.to_sec(),
            'blocked_path': data.data

        }
        self.dataset_obstacle_check = self.dataset_obstacle_check.append(new_data, ignore_index=True)
        self.dataset_obstacle_check = self.dataset_obstacle_check.dropna()
        rospy.loginfo(f"New data appended: {new_data}")

    def sound_callback(self, data,timestamp):
        # Update the current obstacle check state
        new_data = {
            'timestamp': timestamp.to_sec(),
            'sound': data.data

        }
        self.dataset_sound= self.dataset_sound.append(new_data, ignore_index=True)
        self.dataset_sound= self.dataset_sound.dropna()
        rospy.loginfo(f"New data appended: {new_data}")


if __name__ == '__main__':
    try:
        DataExtractionNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass