#!/usr/bin/env python
import rospy
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import time

# Start time
start_time = time.time()

# Define the MaxEnt IRL objective function

def maxent_irl_objective(theta, X, y):
    # Ensure theta is a NumPy array and reshape it
    theta = np.array(theta).reshape(X.shape[1], y.shape[1])
    
    # Calculate scores
    scores = np.dot(X, theta)
    
    # Compute softmax probabilities
    exp_scores = np.exp(scores - np.max(scores, axis=1, keepdims=True))
    probabilities = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    
    # Calculate negative log likelihood
    log_likelihood = np.sum(np.log(probabilities[np.arange(len(y)), np.argmax(y, axis=1)]))
    # Calculate gradient
    return -log_likelihood



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


def create_reward_network(input_dim):
    model = Sequential()
    model.add(Dense(64, activation='relu', input_shape=(input_dim,)))
    model.add(Dense(28, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(7, activation='softmax'))  # Output reward values for each of the 7 classes
    return model

def maxent_irl_objective_ANN(reward_model, expert_trajectories, all_states):
    # Convert inputs to tensors
    all_states = tf.convert_to_tensor(all_states, dtype=tf.float32)
    expert_trajectories = [tf.convert_to_tensor(traj, dtype=tf.float32) for traj in expert_trajectories]

    # Compute the rewards for all states using the neural network
    all_rewards = reward_model(all_states)

    # Compute the feature expectations for the expert trajectories
    expert_rewards = tf.concat([reward_model(traj) for traj in expert_trajectories], axis=0)

    # Compute the partition function (Z) using softmax over all states
    Z = tf.reduce_sum(tf.exp(all_rewards), axis=1)

    # Compute the log likelihood
    log_likelihood = tf.reduce_sum(expert_rewards - tf.math.log(Z[:, tf.newaxis]))

    return -log_likelihood


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

    y = data['sound']  
    #label_encoder = LabelEncoder()
    #y_encoded = label_encoder.fit_transform(y)
    label_binarizer = LabelBinarizer()
    y_one_hot = label_binarizer.fit_transform(y)
    # Initialize parameters
    
    #initial_theta = np.random.rand(X.shape[1])
    # Initialize parameters with correct shape
    initial_theta = np.random.rand(X.shape[1], y_one_hot.shape[1])
    
   
    # Optimize theta using a suitable optimizer (linear)
    #result = minimize(lambda theta: maxent_irl_objective(theta, X_normalized, y_one_hot), initial_theta,  method='L-BFGS-B')
    #optimal_theta = result.x


    #######################Let's consider a ANN for obtaining the reward function###############################
    from sklearn.model_selection import train_test_split
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.callbacks import EarlyStopping
    import tensorflow as tf
    from tensorflow import keras

    x_train, x_test, y_train, y_test = train_test_split(X_normalized, y_one_hot, test_size=0.10, shuffle=True)


    reward_model = create_reward_network(x_train.shape[1])
    reward_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Early stopping callback
    early_stop = EarlyStopping(monitor='loss', patience=2)

    # Train the model
    hist = reward_model.fit(x_train, y_train, epochs=20, validation_split=0.20, batch_size=128, callbacks=[early_stop])

    # Example expert trajectories and all states (for demonstration purposes)
    # Replace these with your actual data
    expert_trajectories = [x_train]  # Assuming entire x_train is considered as expert trajectories
    all_states = x_train

   # Training loop
    epochs = 100
    accuracy_history = [] 

    for epoch in range(epochs):
        with tf.GradientTape() as tape:
            # Compute the MaxEnt IRL objective
            log_likelihood = maxent_irl_objective_ANN(reward_model, expert_trajectories, all_states)

        # Compute gradients
        gradients = tape.gradient(log_likelihood, reward_model.trainable_variables)

        # Update the weights
        reward_model.optimizer.apply_gradients(zip(gradients, reward_model.trainable_variables))

        if epoch % 10 == 0:
            rospy.loginfo(f'Epoch {epoch}, Log Likelihood: {-log_likelihood}')

        # Evaluate validation accuracy for each epoch
        validation_rewards = reward_model.predict(x_test)
        validation_accuracy = np.mean(np.argmax(validation_rewards, axis=1) == np.argmax(y_test, axis=1))
        accuracy_history.append(validation_accuracy)  # Store accuracy for this epoch

        rospy.loginfo(f'Epoch {epoch}, Validation Accuracy: {validation_accuracy}')

    # Plot accuracy over epochs
    plt.plot(range(epochs), accuracy_history, marker='o')
    plt.xlabel('Epochs')    
    plt.ylabel('Validation Accuracy')
    plt.title('Validation Accuracy for different Epochs')
    plt.grid(True)
    plt.savefig(f'plot_accuracy_ANN.png')
    plt.show()


