#!/usr/bin/env python
import rosbag
import pandas as pd
import pickle
import zipfile

def rosbag_to_dataframe(bag_file):
    data = []

    # Open the bag file
    with rosbag.Bag(bag_file, 'r') as bag:
        # Iterate through the messages in the bag file
        for topic, msg, t in bag.read_messages():
            # Convert ROS time to nanoseconds
            timestamp = t.to_nsec()
            # Append the data to the list
            data.append((timestamp, topic, msg))

    # Create a DataFrame
    df = pd.DataFrame(data, columns=['timestamp', 'topic', 'message'])

    return df

if __name__ == "__main__":
    bag_file = "/home/arjan/2024-05-07-11-23-30.bag"
    dataframe = rosbag_to_dataframe(bag_file)

    print("DataFrame:")
    print(dataframe.head())  # Print the first few rows of the DataFrame

    dataframe.to_csv('/home/arjan/Desktop/ros_noetic_base_2204/Data/test_set.txt')
    
   
