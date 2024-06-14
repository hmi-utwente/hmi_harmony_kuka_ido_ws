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

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import KFold

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

def ANN():
    kf = KFold(n_splits=5)
    epochs = 20
    overall_accuracy_history = []
    overall_accuracy_train_history = []
    best_model_path = ''
    best_val_accuracy = 0.0
    #x_train, x_test, y_train, y_test = train_test_split(X_normalized, y_one_hot, test_size=0.10, shuffle=True)

    for fold, (train_index, val_index) in enumerate(kf.split(X_normalized)):
        rospy.loginfo(f'Fold {fold+1}')
        x_train_fold, x_val_fold = X_normalized[train_index], X_normalized[val_index]
        y_train_fold, y_val_fold = y_one_hot[train_index], y_one_hot[val_index]

        reward_model = create_reward_network(X_normalized.shape[1])
        reward_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        early_stop = EarlyStopping(monitor='loss', patience=2)
        history = reward_model.fit(x_train_fold, y_train_fold, epochs=20, validation_split=0.20, batch_size=128, callbacks=[early_stop])


        expert_trajectories = [x_train_fold]  # Replace with your actual expert trajectories
        all_states = x_train_fold

        accuracy_history = []
        accuracy_history_train = []

        for epoch in range(epochs):
            with tf.GradientTape() as tape:
                log_likelihood = maxent_irl_objective_ANN(reward_model, expert_trajectories, all_states)

            gradients = tape.gradient(log_likelihood, reward_model.trainable_variables)
            reward_model.optimizer.apply_gradients(zip(gradients, reward_model.trainable_variables))

            if epoch % 10 == 0:
                rospy.loginfo(f'Epoch {epoch}, Log Likelihood: {-log_likelihood}')

            validation_rewards = reward_model.predict(x_val_fold)
            validation_accuracy = np.mean(np.argmax(validation_rewards, axis=1) == np.argmax(y_val_fold, axis=1))
          

            accuracy_history.append(validation_accuracy)
            train_rewards = reward_model.predict(x_train_fold)
            train_accuracy = np.mean(np.argmax(train_rewards, axis=1) == np.argmax(y_train_fold, axis=1))
            accuracy_history_train.append(train_accuracy)
            rospy.loginfo(f'Epoch {epoch}, Train  Accuracy: {train_accuracy}')
            rospy.loginfo(f'Epoch {epoch}, Validation Accuracy: {validation_accuracy}')

        overall_accuracy_history.append(accuracy_history)
        overall_accuracy_train_history.append(accuracy_history_train)

        best_model_path = f'reward_model_fold_{fold+1}_final_epoch.h5'
        reward_model.save(best_model_path)
        rospy.loginfo(f'Saved model for fold {fold+1} at final epoch: {best_model_path}')


    # Compute the mean accuracy over all folds for each epoch
    mean_accuracy_history = np.mean(overall_accuracy_history, axis=0)
    mean_train_accuracy_history =  np.mean(overall_accuracy_train_history, axis=0)
    # Plotting
    plt.plot(range(epochs), mean_accuracy_history, marker='o', label='Validation Accuracy')
    plt.plot(range(epochs), mean_train_accuracy_history, marker = 'o', label = 'Training Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.title('Accuracy for different Epochs (5-Fold Cross-Validation)')
    plt.legend()
    plt.grid(True)
    plt.xticks(range(epochs))
    plt.savefig(f'plot_accuracy_ANN.png')
    plt.show()


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

    ANN()
    


    
