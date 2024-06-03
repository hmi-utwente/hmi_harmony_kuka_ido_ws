#!/usr/bin/env python
import rospy
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import time

# Start time
start_time = time.time()

# Define the MaxEnt IRL objective function
def maxent_irl_objective(theta, X, y):
    # Ensure theta is a NumPy array
    theta = np.array(theta)
    
    # Calculate scores
    scores = np.dot(X, theta)
    
    # Ensure y is a NumPy array
    y = np.array(y)
    
    # Calculate log likelihood
    log_likelihood = np.sum(np.multiply(scores, y) - np.log(1 + np.exp(scores)))

    # Calculate gradient
    probabilities = 1 / (1 + np.exp(-scores))
    gradient = np.dot(X.T, y - probabilities)

    return -log_likelihood, -gradient


def extract_features(pixel_x, pixel_y, point_z, score, blocked_path):
    # You can modify this function as needed based on your feature extraction logic
    return np.array([pixel_x, pixel_y, point_z, score, blocked_path])

# Calculate reward function
def calculate_reward(state_action_pair, theta):
    # Extract features for the state-action pair
    features = extract_features(*state_action_pair)
    
    # Calculate reward using dot product of features and theta
    reward = np.dot(theta, features)
    
    return reward

if __name__ == '__main__':
    rospy.init_node('irl_node')

    csv_files = [
    '/home/arjan/Desktop/data/data_processed_csv/large_dataset_part_1.csv',
    '/home/arjan/Desktop/data/data_processed_csv/large_dataset_part_2.csv',
    '/home/arjan/Desktop/data/data_processed_csv/large_dataset_part_3.csv',
    '/home/arjan/Desktop/data/data_processed_csv/large_dataset_part_4.csv',
    '/home/arjan/Desktop/data/data_processed_csv/large_dataset_part_5.csv',
    '/home/arjan/Desktop/data/data_processed_csv/large_dataset_part_6.csv',
    '/home/arjan/Desktop/data/data_processed_csv/large_dataset_part_7.csv'
]

    # Read the CSV files into a single DataFrame
    data_frames = [pd.read_csv(file) for file in csv_files]
    data = pd.concat(data_frames, ignore_index=True)
    data['blocked_path'] = data['blocked_path'].apply(lambda x: 1 if x == 'Path is blocked. Obstacle detected.' else 0)
    # Extract features and labels
    X = data[['person_id','body_part_id','pixel_x', 'pixel_y', 'point_z', 'score', 'blocked_path']].values
    scaler = StandardScaler()
    #Fit the scaler to the data and transform X
    X_normalized = scaler.fit_transform(X)

    y = data['sound'].values  # Assuming 'sound' is your label
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # Initialize parameters
    initial_theta = np.random.rand(X.shape[1])

    # Optimize theta using a suitable optimizer
    result = minimize(lambda theta: maxent_irl_objective(theta, X_normalized, y_encoded), initial_theta, jac=True, method='L-BFGS-B')

    # Optimal parameters
    optimal_theta = result.x
    #total_states = len(data)
    #rewards = []
    #for index, row in data.iterrows():
    #    state_action_pair = row[['pixel_x', 'pixel_y', 'point_z', 'score', 'blocked_path']].values
    #    reward = calculate_reward(state_action_pair, optimal_theta)
    #    rewards.append(reward)
    #    progress = (index + 1) / total_states * 100
    #    elapsed_time = time.time() - start_time
    
        # Log the progress as a percentage
   #     rospy.loginfo("Progress: %.2f%%, Elapsed Time: %.2f seconds" % (progress, elapsed_time))    

    # Add rewards to the DataFrame
   # data['reward'] = rewards
    rospy.loginfo(optimal_theta)


