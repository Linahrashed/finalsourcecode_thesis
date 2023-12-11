import os
from pydub import AudioSegment

# preprocess the data

# Specify the path to the directory containing the audio files
audio_directory = 'C:\\Users\\G8\\Downloads\\new dataset\\LibriSpeech\\dev-clean\\84\\121123'

# Specify the name of the specific FLAC file you want to convert
input_flac_filename = '84-121123-0000.flac'

# Check if the specified directory exists
if os.path.exists(audio_directory):
    # Check if the input FLAC file exists in the directory
    flac_filepath = os.path.join(audio_directory, input_flac_filename)
    if os.path.exists(flac_filepath):
        # Define the output WAV file path
        wav_filepath = os.path.join(audio_directory, input_flac_filename[:-5] + '.wav')

        # Convert FLAC to WAV
        audio = AudioSegment.from_file(flac_filepath, format='flac')
        audio.export(wav_filepath, format='wav')

        print(f"Converted {flac_filepath} to {wav_filepath}")
    else:
        print(f"FLAC file '{input_flac_filename}' not found in '{audio_directory}'.")
else:
    print(f"Directory '{audio_directory}' does not exist.")
