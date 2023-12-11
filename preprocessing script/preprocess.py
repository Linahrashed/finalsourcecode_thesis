import librosa
import numpy as np
import os
import soundfile as sf


# Set the directories for train, test, and validation subsets
train_dir = 'C:\\Users\\G8\\Downloads\\new dataset\\LibriSpeech\\train-clean-100'
test_dir = 'C:\\Users\\G8\\Downloads\\new dataset\\LibriSpeech\\test-clean'
val_dir = 'C:\\Users\\G8\\Downloads\\new dataset\\LibriSpeech\\dev-clean'

# Loop through all the audio files in the train subset directory
for root, dirs, files in os.walk(train_dir):
    for audio_file in files:
        if audio_file.endswith('.wav'):
            # Load the audio file and convert it to 16-bit PCM WAV format (we need this format ashan da el tactron bey accept b rate 22050, maktoob taht)
            audio_path = os.path.join(root, audio_file)
            print(f"latest path: {audio_path}.")
            y, sr = librosa.load(audio_path, sr=16000, mono=True)
            #librosa.output.write_wav(audio_path, y, sr=sr, norm=True, bitrate='16')
            sf.write(audio_path, y, sr, subtype='PCM_16')


            # Extract the mel spectrogram and save it as a numpy array
            mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=80, hop_length=256, n_fft=1024, fmin=0.0, fmax=8000.0)
            log_mel = librosa.amplitude_to_db(mel, ref=np.max)
            np.save(os.path.join(train_dir, audio_file.split('.')[0] + '.npy'), log_mel)


# Loop through all the audio files in the test subset directory
for root, dirs, files in os.walk(test_dir):
    for audio_file in files:
        if audio_file.endswith('.wav'):
            # Load the audio file and convert it to 16-bit PCM WAV format
            audio_path = os.path.join(root, audio_file)
            y, sr = librosa.load(audio_path, sr=16000, mono=True)
            #librosa.output.write_wav(audio_path, y, sr=sr, norm=True, bitrate='16')
            sf.write(audio_path, y, sr, subtype='PCM_16')


            # Extract the mel spectrogram and save it as a numpy array
            mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=80, hop_length=256, n_fft=1024, fmin=0.0, fmax=8000.0)
            log_mel = librosa.amplitude_to_db(mel, ref=np.max)
            np.save(os.path.join(test_dir, audio_file.split('.')[0] + '.npy'), log_mel)


# Loop through all the audio files in the validation subset directory
for root, dirs, files in os.walk(val_dir):
    for audio_file in files:
        if audio_file.endswith('.wav'):
            # Load the audio file and convert it to 16-bit PCM WAV format
            audio_path = os.path.join(root, audio_file);
            y, sr = librosa.load(audio_path, sr=16000, mono=True)
            #librosa.output.write_wav(audio_path, y, sr=sr, norm=True, bitrate='16')
            sf.write(audio_path, y, sr, subtype='PCM_16')


            # Extract the mel spectrogram and save it as a numpy array
            mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=80, hop_length=256, n_fft=1024, fmin=0.0, fmax=8000.0)
            log_mel = librosa.amplitude_to_db(mel, ref=np.max)
            np.save(os.path.join(val_dir, audio_file.split('.')[0] + '.npy'), log_mel)


        # # law ayzeen baa we plot the spectogram to check law el preprocessign sah


        # # Plot the mel spectrogram
        # librosa.display.specshow(log_mel, sr=sr, hop_length=256, x_axis='time', y_axis='mel')
        # plt.colorbar(format='%+2.0f dB')
        # plt.title('Mel spectrogram')
        # plt.show()

