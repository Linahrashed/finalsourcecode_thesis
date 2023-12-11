import re
import sys
import numpy as np
import torch
import soundfile as sf

#this file is used to convert text to audio for the frontend design: react app

# Adjust the sys.path as needed
sys.path.append('C:\\Users\\G8\\Documents\\cloned tacotron\\tacotron2\\waveglow')

from hparams import create_hparams
from model import Tacotron2
from layers import TacotronSTFT, STFT
from audio_processing import griffin_lim
from train import load_model
from text import text_to_sequence
from waveglow.denoiser import Denoiser

# Get the input text from command line argument
# input_text = sys.argv[1]
# input_text = """There was something off. I couldn’t put my finger on what exactly it was, but it was definitely there. Yes, something was out of balance, I decided as I stepped off the bus and onto the sidewalk outside John F Kennedy Prep The place looked like it did almost every other day, with its red bricks, bright-colored banners strung up everywhere, and the jumble of students lingering around outside the front doors. The school had been around for more than a century, and it had that Old New York feel. Nothing was ever out of the ordinary. Yet the gray clouds rolling in across the sky felt smothering, bringing with them a feeling of suspicion and . . . sadness. An almost suffocating sadness. New York was the city that never slept, the place that had a thousand different attitudes. But I’d never felt one like this before. “C’mon, Hadley, you’re in the way.” I quickly moved to the side as Taylor Lewis, my best friend, sauntered off the bus. I first met Taylor during freshman orientation, when I’d been wandering the halls alone while looking for my classes. From that moment onward, she’d decided to take me under her wing because we were both wearing the same shirt from American Apparel, and decided to teach me everything she already knew about the social scene at JFK. Without her, I would have been totally lost—literally, figuratively, and most certainly socially. Now, more than two years later, we were still best friends, and I was still content to hang out in Taylor’s social-butterfly shadow. “Why do you have that weird look on your face?” Taylor asked as we followed the throng of people through the front doors. I glanced away from a group of teachers huddled together in the hallway by the front office, their heads together, whispering, and frowned at Taylor. “What look?” She rolled her eyes and gave me a nudge with her elbow. “Never mind. Are you ready for that test in American Government today? I can barely understand what Monroe’s talking about half the time, and I swear, it’s totally pointless that we even know how many cabinet members there are or whatever, and I— Hadley, are you even listening to me?” My focus was drawn to the pair of uniformed police officers located down the hallway from my locker, standing with the principal, Ms. Greene. By the stiff, grim expressions on their faces, I guessed they must have been talking about something highly unpleasant. But what would have brought the police to our high school? “I’m sorry, Taylor, I’m just . . .” I couldn’t come up with a word to describe how off I felt. “I don’t know, just worried about the test too, I guess.” Taylor snorted out a laugh as I rummaged around in my locker for my chemistry textbook. “Why are you worried, Hadley? You’re, like, the only one who actually manages to stay awake in Monroe’s class.” “Guess I’m just lucky.” That, or I had a lawyer for a dad who would flip if I didn’t keep a decent grade in Government. I left Taylor and made for homeroom, now feeling as though someone was following close behind me, breathing down my neck. I dropped into a seat toward the front of the class and focused on keeping my breathing in a steady pattern, succeeding until the first bell rang and our teacher didn’t appear. Mrs. Anderson, the German teacher who ran our homeroom, was probably the nicest person I’d ever met. She was almost always humming under her breath, and had a thousand-watt smile for every person who just happened to look her way. I didn’t have the patience to learn German—I’d barely made it through my two required years of Spanish—but Mrs. Anderson seemed like a hoot, and she made homeroom bearable despite it being so ridiculously early in the morning."""
file_path = sys.argv[1]
with open(file_path, 'r', encoding='utf-8') as file:
    input_text = file.read()

# Create hyperparameters
hparams = create_hparams()
hparams['sampling_rate'] = 22050

# Load Tacotron2 model
checkpoint_path = "C:\\Users\\G8\\Documents\\cloned tacotron\\tacotron2\\checkpoint_133000"
model = load_model(hparams)
model.load_state_dict(torch.load(checkpoint_path)['state_dict'])
_ = model.cuda().eval().half()

# Load WaveGlow model
waveglow_path = 'C:\\Users\\G8\\Documents\\cloned tacotron\\tacotron2\\waveglow_256channels.pt'
waveglow = torch.load(waveglow_path)['model']
waveglow.cuda().eval().half()
for k in waveglow.convinv:
    k.float()
denoiser = Denoiser(waveglow)

# Segment text into chunks of 380 characters (approx. 75 words)
def segment_text(text, max_length):
    sentences = re.split(r'(?<=[.!?]) +', text)
    segments = []
    current_segment = ""

    for sentence in sentences:
        if len(current_segment) + len(sentence) <= max_length:
            current_segment += sentence + " "
        else:
            segments.append(current_segment.strip())
            current_segment = sentence + " "
    if current_segment:
        segments.append(current_segment.strip())

    return segments

max_length = 380
text_segments = segment_text(input_text, max_length)

# Generate and save audio for each segment
for i, segment in enumerate(text_segments):
    sequence = np.array(text_to_sequence(segment, ['english_cleaners']))[None, :]
    sequence = torch.autograd.Variable(torch.from_numpy(sequence)).cuda().long()
    mel_outputs, mel_outputs_postnet, _, _ = model.inference(sequence)

    with torch.no_grad():
        audio = waveglow.infer(mel_outputs_postnet, sigma=0.666)
        audio_denoised = denoiser(audio, strength=0.01)[:, 0]

    output_path = f'C:\\Users\\G8\\Desktop\\ThesisFrontend\\audiobook\\outputAudio\\output_audio_segment_{i+1}.wav'
    audio_denoised_numpy = audio_denoised.cpu().numpy().astype('float32').flatten()
    sf.write(output_path, audio_denoised_numpy, hparams['sampling_rate'])

# Concatenate audio from all segments
audio_files = [f'C:\\Users\\G8\\Desktop\\ThesisFrontend\\audiobook\\outputAudio\\output_audio_segment_{i+1}.wav' for i in range(len(text_segments))]
concatenated_audio = []

for file in audio_files:
    audio, sample_rate = sf.read(file)
    concatenated_audio.append(audio)

concatenated_audio = np.concatenate(concatenated_audio, axis=0)
output_concatenated_path = 'C:\\Users\\G8\\Desktop\\ThesisFrontend\\audiobook\\outputAudio\\concatenated_audio_output_f.wav'
sf.write(output_concatenated_path, concatenated_audio, sample_rate)

# if __name__ == "__main__":
#     # Example command line usage: python script.py "Your text here"
#     main()
