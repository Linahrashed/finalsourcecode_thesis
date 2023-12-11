"""
#Building Train Transcript
import os

# Specify the path to the LibriSpeech dataset root directory
librispeech_root = 'C:\\Users\\G8\\Downloads\\new dataset\\LibriSpeech\\dev-clean'

# Specify the output transcript file
output_transcript_file = 'Train_librispeech_transcript.txt'

# Initialize an empty list to store transcript lines
transcript_lines = []

# Recursively search for transcript files and concatenate their contents
for root, dirs, files in os.walk(librispeech_root):
    for file in files:
        if file.endswith('.trans.txt'):
            transcript_file_path = os.path.join(root, file)
            with open(transcript_file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split(' ', 1)
                    if len(parts) == 2:
                        audio_file_name = os.path.join(root, parts[0] + '.wav')
                        transcript_line = f"{audio_file_name}|{parts[1]}"
                        transcript_lines.append(transcript_line)

# Write the concatenated transcript lines to the output file
with open(output_transcript_file, 'w', encoding='utf-8') as f:
    f.writelines('\n'.join(transcript_lines))

print(f"Transcript file created: {output_transcript_file}")

"""
#Building Validation Transcript
import os

# Specify the path to the LibriSpeech dataset root directory
librispeech_root = 'C:\\Users\\G8\\Downloads\\new dataset\\LibriSpeech\\train-clean-100'

# Specify the output transcript file
output_transcript_file = 'Train_Transcript_transcript.txt'

# Initialize an empty list to store transcript lines
transcript_lines = []

# Recursively search for transcript files and concatenate their contents
for root, dirs, files in os.walk(librispeech_root):
    for file in files:
        if file.endswith('.trans.txt'):
            transcript_file_path = os.path.join(root, file)
            with open(transcript_file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split(' ', 1)
                    if len(parts) == 2:
                        audio_file_name = os.path.join(root, parts[0] + '.wav')
                        transcript_line = f"{audio_file_name}|{parts[1]}"
                        transcript_lines.append(transcript_line)

# Write the concatenated transcript lines to the output file
with open(output_transcript_file, 'w', encoding='utf-8') as f:
    f.writelines('\n'.join(transcript_lines))

print(f"Transcript file created: {output_transcript_file}")