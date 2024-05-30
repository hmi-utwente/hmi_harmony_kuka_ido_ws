#!/usr/bin/env python3
import rospy
import numpy as np
import pandas as pd

def compute_feature_expectations(trajectories, feature_matrix):
    feature_expectations = np.zeros(feature_matrix.shape[1])
    for state, action in trajectories:
        feature = np.concatenate((state[0], [state[1]]))  # Combine pose and blockage info
        feature_expectations += feature
    return feature_expectations / len(trajectories)

def softmax(x):
    return np.exp(x - np.max(x)) / np.sum(np.exp(x - np.max(x)), axis=0)

def compute_policy(feature_matrix, theta):
    rewards = feature_matrix.dot(theta)
    policy = softmax(rewards)
    return policy

def compute_gradient(feature_expectations_expert, feature_matrix, theta):
    policy = compute_policy(feature_matrix, theta)
    feature_expectations_policy = feature_matrix.T.dot(policy)
    gradient = feature_expectations_expert - feature_expectations_policy
    return gradient

def max_ent_irl(env, feature_expectations_expert, learning_rate=0.01, iterations=100):
    theta = np.random.rand(env.feature_matrix.shape[1])
    for _ in range(iterations):
        gradient = compute_gradient(feature_expectations_expert, env.feature_matrix, theta)
        theta += learning_rate * gradient
    return theta

if __name__ == '__main__':
    rospy.init_node('irl_node')

    # Retrieve data from parameters set by data_extraction_node
    extracted_data = rospy.get_param('extracted_data')
    dataset = pd.DataFrame.from_dict(extracted_data)
    
    # Assuming obstacle_check is 1 if obstacle is present, 0 otherwise
    dataset['obstacle_check'] = dataset['obstacle_check'].apply(lambda x: 1 if x == 'Path is blocked. Obstacle detected.' else 0)
    
    feature_matrix = dataset[['pixel_x', 'pixel_y', 'point_z', 'score', 'obstacle_check']].dropna().values
    action_data = dataset['obstacle_check'].dropna().values
    num_actions = len(set(action_data))

    class Environment:
        def __init__(self, feature_matrix, num_actions):
            self.feature_matrix = feature_matrix
            self.num_actions = num_actions

    env = Environment(feature_matrix, num_actions)
    trajectories = [(state, action) for state, action in zip(feature_matrix, action_data)]
    feature_expectations_expert = compute_feature_expectations(trajectories, env.feature_matrix)
    theta = max_ent_irl(env, feature_expectations_expert)

    rospy.set_param('irl_theta', theta.tolist())
    rospy.loginfo(f"Learned reward weights: {theta}")
