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
from ros_openpose.msg import Frame  
from std_msgs.msg import String

import time
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import KFold

from math import floor
import pickle
from sklearn.metrics import precision_score
import gym
from collections import deque

from sklearn.model_selection import train_test_split
import random
        



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
    epochs = 50
    overall_accuracy_history = []
    overall_accuracy_train_history = []
    overall_precision_history = []
    overall_precision_train_history = []
    best_model_path = ''
    best_val_accuracy = 0.0

    for fold, (train_index, val_index) in enumerate(kf.split(X_normalized)):
        rospy.loginfo(f'Fold {fold+1}')
        x_train_fold, x_val_fold = X_normalized[train_index], X_normalized[val_index]
        y_train_fold, y_val_fold = y_one_hot[train_index], y_one_hot[val_index]

        reward_model = create_reward_network(X_normalized.shape[1])
        reward_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        early_stop = EarlyStopping(monitor='loss', patience=2)
        history = reward_model.fit(x_train_fold, y_train_fold, epochs=50, validation_split=0.20, batch_size=128, callbacks=[early_stop])

        expert_trajectories = [x_train_fold]  # Replace with your actual expert trajectories
        all_states = x_train_fold

        accuracy_history = []
        accuracy_history_train = []
        precision_history = []
        precision_history_train = []

        for epoch in range(epochs):
            with tf.GradientTape() as tape:
                log_likelihood = maxent_irl_objective_ANN(reward_model, expert_trajectories, all_states)

            gradients = tape.gradient(log_likelihood, reward_model.trainable_variables)
            reward_model.optimizer.apply_gradients(zip(gradients, reward_model.trainable_variables))

            if epoch % 10 == 0:
                rospy.loginfo(f'Epoch {epoch}, Log Likelihood: {-log_likelihood}')

            validation_rewards = reward_model.predict(x_val_fold)
            validation_preds = np.argmax(validation_rewards, axis=1)
            y_val_true = np.argmax(y_val_fold, axis=1)
            validation_accuracy = np.mean(validation_preds == y_val_true)

            train_rewards = reward_model.predict(x_train_fold)
            train_preds = np.argmax(train_rewards, axis=1)
            y_train_true = np.argmax(y_train_fold, axis=1)
            train_accuracy = np.mean(train_preds == y_train_true)

            # Compute precision
            validation_precision = precision_score(y_val_true, validation_preds, average='macro')
            train_precision = precision_score(y_train_true, train_preds, average='macro')

            accuracy_history.append(validation_accuracy)
            accuracy_history_train.append(train_accuracy)
            precision_history.append(validation_precision)
            precision_history_train.append(train_precision)

            rospy.loginfo(f'Epoch {epoch}, Train Accuracy: {train_accuracy}, Train Precision: {train_precision}')
            rospy.loginfo(f'Epoch {epoch}, Validation Accuracy: {validation_accuracy}, Validation Precision: {validation_precision}')

        overall_accuracy_history.append(accuracy_history)
        overall_accuracy_train_history.append(accuracy_history_train)
        overall_precision_history.append(precision_history)
        overall_precision_train_history.append(precision_history_train)

        best_model_path = f'reward_model_fold_{fold+1}_final_epoch.h5'
        reward_model.save(best_model_path)
        rospy.loginfo(f'Saved model for fold {fold+1} at final epoch: {best_model_path}')

    # Compute the mean accuracy and precision over all folds for each epoch
    mean_accuracy_history = np.mean(overall_accuracy_history, axis=0)
    mean_train_accuracy_history = np.mean(overall_accuracy_train_history, axis=0)
    mean_precision_history = np.mean(overall_precision_history, axis=0)
    mean_train_precision_history = np.mean(overall_precision_train_history, axis=0)

    # Plotting Accuracy
    plt.plot(range(epochs), mean_accuracy_history, marker='o', label='Validation Accuracy')
    plt.plot(range(epochs), mean_train_accuracy_history, marker='o', label='Training Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.title('Accuracy for different Epochs (5-Fold Cross-Validation)')
    plt.legend()
    plt.grid(True)
    plt.xticks(range(epochs))
    plt.savefig('plot_accuracy_ANN.png')
    plt.show()

    # Plotting Precision
    plt.plot(range(epochs), mean_precision_history, marker='o', label='Validation Precision')
    plt.plot(range(epochs), mean_train_precision_history, marker='o', label='Training Precision')
    plt.xlabel('Epochs')
    plt.ylabel('Precision')
    plt.title('Precision for different Epochs (5-Fold Cross-Validation)')
    plt.legend()
    plt.grid(True)
    plt.xticks(range(epochs))
    plt.savefig('plot_precision_ANN.png')
    plt.show()

class RealTimeDataNode:
    def __init__(self):
        rospy.init_node('real_time_data_node')
        self.dataset_openpose = pd.DataFrame(columns=['timestamp', 'person_id', 'body_part_id', 'pixel_x', 'pixel_y', 'point_z', 'score'])
        self.dataset_obstacle_check = pd.DataFrame(columns=['timestamp', 'blocked_path'])
        self.dataset_sound = pd.DataFrame(columns=['timestamp', 'sound'])

        self.openpose_sub = rospy.Subscriber('/frame', Frame, self.frame_callback)
        self.obstacle_check_sub = rospy.Subscriber('obstacle_check', String, self.obstacle_check_callback)
        self.sound_sub = rospy.Subscriber('/sound_command', String, self.sound_callback)

        rospy.loginfo("Real-time data node initialized and subscribers set up.")

    def frame_callback(self, data):
        timestamp = rospy.get_rostime().to_sec()
        new_data = []
        for person_id, person in enumerate(data.persons):
            for body_part_id, body_part in enumerate(person.bodyParts):
                new_data.append({
                    'timestamp': timestamp,
                    'person_id': person_id,
                    'body_part_id': body_part_id,
                    'pixel_x': body_part.pixel.x,
                    'pixel_y': body_part.pixel.y,
                    'point_z': body_part.point.z,
                    'score': body_part.score
                })
        self.dataset_openpose = self.dataset_openpose.append(new_data, ignore_index=True)
        self.dataset_openpose.dropna(inplace=True)
        
    def obstacle_check_callback(self, data):
        timestamp = rospy.get_rostime().to_sec()
        blocked_path = 1 if data.data == 'Path is blocked. Obstacle detected.' else 0
        new_data = {
            'timestamp': timestamp,
            'blocked_path': blocked_path
        }
        self.dataset_obstacle_check = self.dataset_obstacle_check.append(new_data, ignore_index=True)
        self.dataset_obstacle_check.dropna(inplace=True)
       
    def sound_callback(self, data):
        timestamp = rospy.get_rostime().to_sec()
        new_data = {
            'timestamp': timestamp,
            'sound': data.data
        }
        self.dataset_sound = self.dataset_sound.append(new_data, ignore_index=True)
        self.dataset_sound.dropna(inplace=True)

    def merge_datasets(self):
        current_timestamp = floor(rospy.get_time())
    
        # Assuming each dataset has at least 500 rows
        openpose_latest = self.dataset_openpose[-500:]
        obstacle_check_latest = self.dataset_obstacle_check[-500:]
        sound_latest = self.dataset_sound[-500:]
    
        openpose_latest['timestamp'] = openpose_latest['timestamp'].apply(lambda x: floor(x)).astype(float)
        obstacle_check_latest['timestamp'] = obstacle_check_latest['timestamp'].apply(lambda x: floor(x)).astype(float)
        sound_latest['timestamp'] = sound_latest['timestamp'].apply(lambda x: floor(x)).astype(float)
    
        self.merged_dataset = pd.merge(openpose_latest, obstacle_check_latest, on='timestamp', how='outer')
        self.merged_dataset = pd.merge(self.merged_dataset, sound_latest, on='timestamp', how='left')
        self.merged_dataset['sound'].fillna('no_sound', inplace=True)
    
        rospy.set_param("merged_data", self.merged_dataset.to_dict(orient='list'))
        rospy.loginfo("Data merged and parameter set for the latest 500 rows.")

        openpose_current = openpose_latest[openpose_latest['timestamp'] == current_timestamp]
        obstacle_check_current = obstacle_check_latest[obstacle_check_latest['timestamp'] == current_timestamp]
        sound_current = sound_latest[sound_latest['timestamp'] == current_timestamp]

        merged_current = pd.merge(openpose_current, obstacle_check_current, on='timestamp', how='outer')
        merged_current = pd.merge(merged_current, sound_current, on='timestamp', how='left')
        merged_current['sound'].fillna('no_sound', inplace=True)

        self.merged_dataset_fitted = merged_current[['person_id','body_part_id','pixel_x', 'pixel_y', 'point_z', 'score', 'blocked_path']].values

        with open('/home/arjan/Desktop/data/data_processed_csv/scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
    
        try:
            self.merged_dataset_fitted = scaler.transform(self.merged_dataset_fitted)
        except Exception as e:
            rospy.logerr(f"Error in scaling dataset: {e}")


    def run(self):
        idx = 0
        rate = rospy.Rate(1)  # Adjust the rate as needed
        while not idx == 5:
            self.merge_datasets()
            idx += 1
        return self.merged_dataset_fitted



class CustomEnv(gym.Env):
    def __init__(self, reward_model, state_shape, node):
        super(CustomEnv, self).__init__()
        self.reward_model = reward_model
        self.state_shape = state_shape
        self.action_space_shape = 7  # Size of the action space array
        self.action_space = gym.spaces.Box(low=0, high=1, shape=(self.action_space_shape,), dtype=np.float32)  # Box space for action array
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=state_shape, dtype=np.float32)
        self.state = node.merged_dataset_fitted
        self.last_action_time = time.time() 
        self.last_action = None

 
    def step(self, action):
        # Ensure minimum time interval between actions
        current_time = time.time()
        time_since_last_action = current_time - self.last_action_time
        if time_since_last_action < 5.0:  # Adjust 1.0 second as needed
            time.sleep(5.0 - time_since_last_action)  # Wait to enforce minimum interval

        if self.last_action == action and time_since_last_action < 15.0:
            # Skip action execution
            reward = 0.0  # Set a zero reward or penalty for skipping
            done = False  # Assuming episode is not done
            return self.state, reward, done, {}
        
        # Update last action time
        self.last_action = action
        self.last_action_time = time.time()

        # Execute the action (play the sound)
        #self._play_sound(action)
        rospy.loginfo("Play sound {action}" )
        # Define how to get the next state
        state = self._get_state()

        # Define condition to end the episode
        done = self._check_done(state)

        # Get reward from ANN model
        reward = self._get_reward(state)

        # Return state, reward, done, and additional info (empty for now)
        return state, reward, done, {}
    

    def reset(self):
        state = self._reset_state()  # Define this method to reset the environment
        self.last_action_time = time.time()
        self.last_action = None  # Reset last action after reset
        return state

    #def _get_reward(self, state):
    #    state = np.expand_dims(state, axis=0)  # Add batch dimension
    #    reward_prediction = self.reward_model.predict(state)
    #    return np.max(reward_prediction)
    
    def _get_reward(self, state):
        reward_prediction = self.reward_model.predict(state)
        return np.max(reward_prediction)


    def _get_state(self):
        # Define how to get the next state
        #pass
        return self.state

    def _check_done(self, state):
        # Define condition to end the episode
        pass

    def _reset_state(self):
        # Define how to reset the environment
        return node.run()


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=1000)
        self.gamma = 0.95    # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        rospy.loginfo(act_values[0])
        return np.argmax(act_values[0])

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = (reward + self.gamma *
                          np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            old_action = np.argmax(target_f[0])  # Get the old action before updating
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
            new_action = np.argmax(target_f[0])  # Get the new action after updating
            print(f"State: {state}, Old Action: {old_action}, New Action: {new_action}")
        
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        if not name.endswith('.weights.h5'):
            name += '.weights.h5'
        self.model.save_weights(name)


if __name__ == '__main__':
    
    reward_retrieval = 0  #0: run the real-time RL; 1: run ANN for reward function
    
    if reward_retrieval == 1:
    
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
        with open('/home/arjan/Desktop/data/data_processed_csv/scaler.pkl', 'wb') as f:
            pickle.dump(scaler, f)

        y = data['sound']  
        #label_encoder = LabelEncoder()
        #y_encoded = label_encoder.fit_transform(y)
        label_binarizer = LabelBinarizer()
        y_one_hot = label_binarizer.fit_transform(y)

        with open('/home/arjan/Desktop/data/data_processed_csv/label_binarizer.pkl', 'wb') as f:
            pickle.dump(label_binarizer, f)



        # Initialize parameters
    
        #initial_theta = np.random.rand(X.shape[1])
        # Initialize parameters with correct shape
        initial_theta = np.random.rand(X.shape[1], y_one_hot.shape[1])
    
   
        # Optimize theta using a suitable optimizer (linear)
        #result = minimize(lambda theta: maxent_irl_objective(theta, X_normalized, y_one_hot), initial_theta,  method='L-BFGS-B')
        #optimal_theta = result.x


        #######################Let's consider a ANN for obtaining the reward function###############################

        ANN()
    else:
        try:
            node = RealTimeDataNode()
            node.run()
        

             # Initialize the reward model (assumed to be already trained)
            reward_model = tf.keras.models.load_model('/home/arjan/Desktop/ros_noetic_base_2204/reward_model_fold_5_final_epoch.h5')  # Load or create the reward model here
            
            if hasattr(node, 'merged_dataset_fitted') and node.merged_dataset_fitted is not None:
                #rospy.loginfo(f"Merged dataset fitted shape: {node.merged_dataset_fitted.shape}")
                state_shape = node.merged_dataset_fitted.shape  # Correctly define the shape as a tuple
                #rospy.loginfo(f"State shape: {state_shape}")
                obj = node.merged_dataset_fitted
                env = CustomEnv(reward_model, state_shape,node)

                state_size = env.observation_space.shape[0]
                action_size = env.action_space_shape
                agent = DQNAgent(state_size, action_size)
                done = False
                batch_size = 250
                for e in range(100):
                    state = env.reset()
                    for time in range(60):
                        action = agent.act(state)
                        next_state, reward, done, _ = env.step(action)
                        agent.remember(state, action, reward, next_state, done)
                        state = next_state
                        if done:
                            rospy.loginfo(f"episode: {e}/{1000}, score: {time}, e: {agent.epsilon:.2}")
                            break
                        if len(agent.memory) > batch_size:
                            agent.replay(batch_size)
                        # Save the model weights every 50 episodes
                    if e % 50 == 0:
                    #    agent.save(f"dqn_model_{e}.h5")
                        agent.save(f"dqn_model_{e}.h5")

        except rospy.ROSInterruptException:
            pass



    
