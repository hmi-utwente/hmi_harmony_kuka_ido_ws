import pandas as pd
import os
import numpy as np

def label_data(video_lbl, frame_rate = 15.08):
    df = pd.read_excel('/home/arjan/Desktop/openpose/gestures/gestures/ActionOfInterestTVSubject3.xlsx')
    df_sub1 = df[df['Video'] == video_lbl]
    df_sub1
    # Define the video frame rate (frames per second)

    # Function to determine the action label for a given timestamp
    def get_action_label(timestamp):
        for index, row in df_sub1.iterrows():
            if row['StartTime(Seconds)'] <= timestamp / frame_rate <= row['EndTime(Seconds)']:
                return row['Action']
        return 0  # Return None if no action is found for the timestamp

    action_labels = [get_action_label(timestamp) for timestamp in range(1801)]
    df_json_files = pd.DataFrame()
    df_json_files['Action_Label'] = action_labels
    return df_json_files

# Define the video frame rate (frames per second)
frame_rate = 15.08  # Assuming a frame rate of 15.08 frames per second
df_json_files_v1 = label_data(1, frame_rate)

def import_json_openpose_data(vrs):

    import json

    # Dictionary to store index-label mapping
    json_files_dict = {}

    # Dictionary to store data for each JSON file
    json_data_dict = {}

    # Iterate over the JSON files
    for i in range(1801):
        # Specify the path to the JSON file
        json_file_path = f'/home/arjan/Desktop/openpose/gestures/gestures/output_json_tv{vrs}/video_sub3_tv{vrs}_{i:012}_keypoints.json'

        # Add the index and JSON file path to the dictionary
        json_files_dict[i] = json_file_path

        # Read the contents of the JSON file
        with open(json_file_path, 'r') as f:
            json_data = json.load(f)
    
    # Add the JSON data to the dictionary
        json_data_dict[i] = json_data

    # Now json_files_dict contains the mapping of indices to JSON file paths
    #   The keys are labeled from 0 to 1800, and the values are the corresponding JSON file paths

    # And json_data_dict contains the data from each JSON file
    # The keys are labeled from 0 to 1800, and the values are the JSON data
    return json_data_dict, json_files_dict

#x,src = import_json_openpose_data(1)
#y = label_data(1)['Action_Label']
#pose_keypoints = x[1800]['people'][0]['pose_keypoints_2d']
#y[1800]
predict = True

data_list = []
excel_file_path = '/home/arjan/Desktop/ros_noetic_base_2204/persons/gestures_data_collection.csv'
if os.path.isfile(excel_file_path) and predict:
    existing_df_nw = pd.read_csv(excel_file_path)
    y_add = existing_df_nw['New_Column'].astype(float)
    existing_df_nw = existing_df_nw.drop(columns=['New_Column'])
    x = existing_df_nw
    y = y_add
    y = pd.DataFrame(y)
    y.astype('int32')

    from sklearn.model_selection import train_test_split

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.10,shuffle=True)
    print('Shape of train data is : ',x_train.shape)
    print('Shape of label data is : ',y_train.shape)

    from keras.utils import to_categorical
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    from keras.callbacks import EarlyStopping
    from tensorflow import keras

    early_stop = EarlyStopping(monitor='loss', patience=2)
    model = keras.Sequential()

    model.add(keras.layers.Dense(128, activation='relu', input_shape=(50,)))

    model.add(keras.layers.Dense(256, activation='relu'))

    model.add(keras.layers.Dense(128, activation='relu'))

    model.add(keras.layers.Dense(256, activation='relu'))

    model.add(keras.layers.Dense(128, activation='relu'))

    model.add(keras.layers.Dense(64, activation='relu'))

    model.add(keras.layers.Dense(128, activation='relu'))

    model.add(keras.layers.Dense(256, activation='relu'))

    model.add(keras.layers.Dense(128, activation='relu'))

    model.add(keras.layers.Dense(64, activation='relu'))

    model.add(keras.layers.Dense(13, activation='relu'))

    model.add(keras.layers.Dense(5, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
#model.summary()

    hist = model.fit(x_train , y_train , epochs=6, validation_split=0.20, batch_size= 128,callbacks=[early_stop])

# Assuming model.predict(x_test) gives predictions
#predictions = model.predict(x_test)

# Convert predictions back to normal values
#predicted_labels = np.argmax(predictions, axis=1)

