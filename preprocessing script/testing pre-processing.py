# import os
# import librosa
# import random

# # Set the directory where your processed audio files are stored
# processed_dir = 'C:\\Users\\G8\\Downloads\\newdataset\\LibriSpeech\\train-clean-100'

# # # List the contents of the directory to check for files
# # directory_contents = os.listdir(processed_dir)
# # print(directory_contents)

# # Get a list of processed audio files in the directory
# processed_files = [f for f in os.listdir(processed_dir) if f.endswith('.wav')]

# # Print the list of processed files for debugging
# print(processed_files)

# # Check if there are any processed files in the list
# if processed_files:
#     # Choose a random file from the list
#     selected_file = random.choice(processed_files)
#     selected_audio_path = os.path.join(processed_dir, selected_file)

#     # Load the audio file and get its properties
#     y, sr = librosa.load(selected_audio_path, sr=None, mono=True)
#     duration = librosa.get_duration(y=y, sr=sr)

#     # Print the properties of the selected file
#     print(f"Selected File: {selected_file}")
#     print(f"Sampling Rate: {sr} Hz")
#     print(f"Duration (s): {duration} seconds")
# else:
#     print("No processed audio files found in the directory.")


import os
import librosa
import random

# Set the directory where your processed audio files are stored
processed_dir = 'C:\\Users\\G8\\Downloads\\new dataset\\LibriSpeech\\dev-clean'

# Function to recursively get all files with a specific extension in a directory
def get_files_recursive(directory, extension):
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                matching_files.append(os.path.join(root, file))
    return matching_files

# Get a list of processed audio files in the directory and its subdirectories
processed_files = get_files_recursive(processed_dir, '.wav')

# Check if there are any processed files in the list
if processed_files:
    # Choose a random file from the list
    selected_file = random.choice(processed_files)

    # Load the audio file and get its properties
    y, sr = librosa.load(selected_file, sr=None, mono=True)
    duration = librosa.get_duration(y=y, sr=sr)

    # Print the properties of the selected file
    print(f"Selected File: {selected_file}")
    print(f"Sampling Rate: {sr} Hz")
    print(f"Duration (s): {duration} seconds")
else:
    print("No processed audio files found in the directory.")

