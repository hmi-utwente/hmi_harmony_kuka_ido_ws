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

#def obstacle(scan_msg,valid_ranges):
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
#        obstacle(scan_msg,valid_ranges)
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
from std_msgs.msg import Float64
from sound_play.msg import SoundRequest  #check of dit werkt
from sound_play.libsoundplay import SoundClient #check of dit werkt

from robot_movement.robot_movement_script import RobotMovement as robot_movement
import time
from playsound import playsound
import sys
import re
sys.path.append('/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/my_robot_scan/src/my_robot_scan/')
from gestures_ml_model import *

#Parameters
close_range = 0.7
speed = 10


class Behaviors:
    def __init__(self,stop_rotate, button_press_y, button_press_x, button_press_b, button_press_a):
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
        self.button_press_y = button_press_y
        self.button_press_x = button_press_x
        self.button_press_b = button_press_b
        self.button_press_a = button_press_a
    
    def publish_led_parameters(self):
        # Initialize ROS node
       # rospy.init_node("led_controller_publisher", anonymous=True)
    
        # Create publisher for the parameter updates topic
        pub = rospy.Publisher("/led_controller_node/modes/custom_programs/base_led_animations/animation0/solid/parameter_updates", Float64, queue_size=10)

        r = 0.0
        g = 0.7        # Create a Float64 message with the desired RGB values

        b = 0.34
        a = 1.0
        msg_led= Float64(data=r)
        msg_led.data = g
        msg_led.data = b
        msg_led.data = a

        # Publish the message
        pub.publish(msg_led)
    
    def frame_callback(self, frame_msg):
        if not frame_msg.persons:
            rospy.logwarn("No person detected!")
            self.person_detected = False
        else:
            rospy.logwarn("Person detected!")
            self.person_detected = True
            self.publish_led_parameters() #not resolved yet
            if self.button_press_a:
                self.gestures_expand_data(frame_msg)
                #self.mobility(frame_msg)
    
    def gestures_expand_data(self,frame_msg):
        start_time = time.time()
        larger_array = []
        file_path = "/home/arjan/Desktop/ros_noetic_base_2204/persons/person.txt"
        with open(file_path, "w") as file:
            for part_info in frame_msg.persons:
                file.write(str(part_info))
        # Read the content of the text file
        with open('/home/arjan/Desktop/ros_noetic_base_2204/persons/person.txt', 'r') as file:
            data = file.read()

        # Use regular expressions to find all (x, y) pixel points
        # Use regular expressions to find all (x, y) pixel points
        pixel_points = re.findall(r'pixel:\s+?x:\s*([\d.]+)\s+y:\s*([\d.]+)', data)
        
        # Convert the pixel points to tuples of floats
        pixel_points = [(float(x), float(y)) for x, y in pixel_points]
        flattened_coordinates = [coord for point in pixel_points for coord in point]
        larger_array.append(flattened_coordinates)
        
        df = pd.DataFrame(larger_array)
        #rospy.loginfo(df)

           
        df['New_Column'] = 0 
     

        excel_file_path = '/home/arjan/Desktop/ros_noetic_base_2204/persons/gestures_data_collection.csv'

        if os.path.isfile(excel_file_path):
            existing_df = pd.read_csv(excel_file_path)
            if df.empty:
                print("DataFrame 'df' is empty. No data to append.")
            else:
                # Append data to the first column of existing_df
                df.columns = existing_df.columns
        
                 # Append data to existing_df along rows
                updated_df = pd.concat([existing_df, df], ignore_index=True)
                updated_df.to_csv(excel_file_path, index=False)

        else:
            if df.empty:
                print("DataFrame 'df' is empty. No data to write.")
            else:
            # Write df to a new CSV file
                df.to_csv(excel_file_path, index=False)
        

    def mobility(self,frame_msg):
        start_time = time.time()
        larger_array = []
        file_path = "/home/arjan/Desktop/ros_noetic_base_2204/persons/person.txt"
        with open(file_path, "w") as file:
            for part_info in frame_msg.persons:
                file.write(str(part_info))
        # Read the content of the text file
        with open('/home/arjan/Desktop/ros_noetic_base_2204/persons/person.txt', 'r') as file:
            data = file.read()

        # Use regular expressions to find all (x, y) pixel points
        # Use regular expressions to find all (x, y) pixel points
        pixel_points = re.findall(r'pixel:\s+?x:\s*([\d.]+)\s+y:\s*([\d.]+)', data)
        
        # Convert the pixel points to tuples of floats
        pixel_points = [(float(x), float(y)) for x, y in pixel_points]
        flattened_coordinates = [coord for point in pixel_points for coord in point]
        larger_array.append(flattened_coordinates)
        
        df = pd.DataFrame(larger_array)
        
    
        predictions = model.predict(df)
        predicted_labels = np.argmax(predictions, axis=1)
        rospy.loginfo(predicted_labels)

    def obstacle(self):

        while self.object_detected and not self.stop_rotation:
            
            if self.latest_scan_msg:
                #scan for obstacles
                valid_ranges = [range_val for range_val in self.latest_scan_msg.ranges if not np.isnan(range_val)]
                if valid_ranges:
                    if all(val > close_range for val in valid_ranges):
                        #rospy.loginfo(valid_ranges)
                        self.object_detected = False
                        rospy.loginfo("No obstruction of the way")
                        time.sleep(10)
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
                        
                        if not self.person_detected:
                            idx = 0
                            return_angle = 0
                            if not self.button_press_a and idx < 1: #rotate in steps
                                robot_movement().rotate(math.copysign(1,turning_angle) * (0.5 * math.pi), speed, self.person_detected)
                                rospy.loginfo("Check for people...")
                                time.sleep(15)
                                idx += 1
                                return_angle += np.abs(math.copysign(1,turning_angle) * (0.5 * math.pi))
                                if self.person_detected:
                                    
                                    rospy.loginfo("Person detected, can you help me")
                                    playsound('/home/arjan/Desktop/ML_Human_Actions/ROBOGIB_SRP_EX_NSNAT_NL_033.wav')
                                    time.sleep(15)
                                    
                                    
                                    
                                    robot_movement().rotate(-return_angle, speed, self.person_detected)

                                    
                                    valid_ranges = [range_val for range_val in self.latest_scan_msg.ranges if not np.isnan(range_val)]

                                    if valid_ranges:
                                        while any(val < close_range for val in valid_ranges):
                                            playsound('/home/arjan/Desktop/ML_Human_Actions/ROBOGIB_SAD_EX_NSNAT_NL_032.wav')
                                            time.sleep(15)
                                               
                                        if all(val > close_range for val in valid_ranges):
                                            playsound('/home/arjan/Desktop/ML_Human_Actions/ROBOGIB_SRP_EX_NSNAT_NL_029.wav')
                                        
                                        self.obstacle()


                                else:
                                    rospy.loginfo("no person detected")
                                    playsound('/home/arjan/Desktop/ML_Human_Actions/ROBOGIB_SAD_EX_NSNAT_NL_032.wav')

                            robot_movement().rotate(-return_angle, speed, self.person_detected)
                                            
                            
                            self.stop_rotation = True
                            return
                        else:
                            #rospy.loginfo("Obstacle in the way, can you help?")
                            #playsound('/home/arjan/Desktop/ML_Human_Actions/ROBOGIB_SAD_EX_NSNAT_NL_032.wav')
                            #time.sleep(30)
                            self.obstacle()
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
        if self.object_detected_close_range:
            #rospy.loginfo("Object detected")
            if not self.stop_rotation and self.button_press_y:
                self.obstacle()
            elif self.stop_rotation and self.button_press_y:
                rospy.loginfo("Signaling for help, obstacle in the way")
                playsound('/home/arjan/Desktop/ML_Human_Actions/ROBOGIB_SAD_EX_NSNAT_NL_032.wav')
                time.sleep(5)
                self.stop_rotation = False
                
            #elif self.button_press_a:
                #Do tasks for event A
                #rospy.loginfo("Event A")
            #elif self.button_press_x:
                #Do tasks for event X
                #rospy.loginfo("Event X")
            #elif self.button_press_b:
                #Do tasks for event b
                #rospy.loginfo("Event B")
        else:
            rospy.loginfo("No close object detected")      
            

      

    