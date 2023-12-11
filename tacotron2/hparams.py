""""
import tensorflow as tf
from text import symbols

#import tf_slim as slim 




def create_hparams(hparams_string=None, verbose=False):
    #Create model hyperparameters. Parse nondefault from given string.


    hparams = tf.contrib.training.HParams(
            
        ################################
        # Experiment Parameters        #
        ################################
        epochs=500,
        iters_per_checkpoint=1000,
        seed=1234,
        dynamic_loss_scaling=True,
        fp16_run=False,
        distributed_run=False,
        dist_backend="nccl",
        dist_url="tcp://localhost:54321",
        cudnn_enabled=True,
        cudnn_benchmark=False,
        ignore_layers=['embedding.weight'],

        ################################
        # Data Parameters             #
        ################################
        load_mel_from_disk=False,
        #training_files='filelists/ljs_audio_text_train_filelist.txt',
        training_files='C:\\Users\\G8\\Documents\\LJSpeech-1.1\\ljs_audio_text_train_filelist',
        #validation_files='filelists/ljs_audio_text_val_filelist.txt',
        validation_files='C:\\Users\\G8\\Documents\\LJSpeech-1.1\\ljs_audio_text_val_filelist',


        text_cleaners=['english_cleaners'],

        ################################
        # Audio Parameters             #
        ################################
        max_wav_value=32768.0,
        sampling_rate=22050, #needs to be changed to 16000
        filter_length=1024,
        hop_length=256,
        win_length=1024,
        n_mel_channels=80,
        mel_fmin=0.0,
        mel_fmax=8000.0,

        ################################
        # Model Parameters             #
        ################################
        n_symbols=len(symbols),
        symbols_embedding_dim=512,

        # Encoder parameters
        encoder_kernel_size=5,
        encoder_n_convolutions=3,
        encoder_embedding_dim=512,

        # Decoder parameters
        n_frames_per_step=1,  # currently only 1 is supported
        decoder_rnn_dim=1024,
        prenet_dim=256,
        max_decoder_steps=1000,
        gate_threshold=0.5,
        p_attention_dropout=0.1,
        p_decoder_dropout=0.1,

        # Attention parameters
        attention_rnn_dim=1024,
        attention_dim=128,

        # Location Layer parameters
        attention_location_n_filters=32,
        attention_location_kernel_size=31,

        # Mel-post processing network parameters
        postnet_embedding_dim=512,
        postnet_kernel_size=5,
        postnet_n_convolutions=5,

        ################################
        # Optimization Hyperparameters #
        ################################
        use_saved_learning_rate=False,
        learning_rate=1e-3,
        weight_decay=1e-6,
        grad_clip_thresh=1.0,
        batch_size=32, #was 64
        mask_padding=True  # set model's padded outputs to padded values
    )


    
   if  hparams_string:
        tf.logging.info('Parsing command line hparams: %s', hparams_string)
        hparams.parse(hparams_string)

    if verbose:
        tf.logging.info('Final parsed hparams: %s', hparams.values())

    return hparams
"""


import tensorflow as tf
from text import symbols

def create_hparams(hparams_dict=None, verbose=False):
    """Create model hyperparameters from a dictionary or use default values."""

    hparams = {
    'epochs': 500,
    'iters_per_checkpoint': 1000,
    'seed': 1234,
    'dynamic_loss_scaling': True,
    'fp16_run': False,
    'distributed_run': False,
    'dist_backend': 'nccl',
    'dist_url': 'tcp://localhost:54321',
    'cudnn_enabled': True,
    'cudnn_benchmark': False,
    'ignore_layers': ['embedding.weight'],

    # # Data Parameters for lj speech
    # 'load_mel_from_disk': False,
    # 'training_files': 'C:\\Users\\G8\\Documents\\LJSpeech-1.1\\ljs_audio_text_train_filelist.txt',
    # 'validation_files': 'C:\\Users\\G8\\Documents\\LJSpeech-1.1\\ljs_audio_text_val_filelist.txt',
    # 'text_cleaners': ['english_cleaners'],

    
  
#   Data Parameters for librispeech
    'load_mel_from_disk': False,
    'training_files': 'C:\\Users\\G8\\Desktop\\fin‌al_librispeech\\train_100_transcript.txt',
    'validation_files': 'C:\\Users\\G8\\Desktop\\fin‌al_librispeech\\val_transcript.txt',
    #'training_files': 'C:\\Users\\G8\\Desktop\\newlib3\\LibriSpeech\\LibriSpeech\\trainClean_metadata.txt',
    #'validation_files': 'C:\\Users\\G8\\Desktop\\newlib3\\LibriSpeech\\LibriSpeech\\val_metadata.txt',
    'text_cleaners': ['english_cleaners'], 

    # Audio Parameters
    'max_wav_value': 32768.0,
    'sampling_rate': 16000,  #was 22050 for lj speech, changed to 16000 for librispeech
    'filter_length': 1024,
    'hop_length': 256, 
    'win_length': 1024,
    'n_mel_channels': 80,
    'mel_fmin': 0.0,
    'mel_fmax': 8000.0,

    # Model Parameters
    'n_symbols': len(symbols),
    'symbols_embedding_dim': 512,

    # Encoder parameters
    'encoder_kernel_size': 5,
    'encoder_n_convolutions': 3,
    'encoder_embedding_dim': 512,

    # Decoder parameters
    'n_frames_per_step': 1,  # currently only 1 is supported
    'decoder_rnn_dim': 1024,
    'prenet_dim': 256,
    'max_decoder_steps': 2500, #was 1000, changed to make output longer
    'gate_threshold': 0.5,
    'p_attention_dropout': 0.1,
    'p_decoder_dropout': 0.1,

    # Attention parameters
    'attention_rnn_dim': 1024,
    'attention_dim': 128,

    # Location Layer parameters
    'attention_location_n_filters': 32,
    'attention_location_kernel_size': 31,

    # Mel-post processing network parameters
    'postnet_embedding_dim': 512,
    'postnet_kernel_size': 5,
    'postnet_n_convolutions': 5,

    # Optimization Hyperparameters
    'use_saved_learning_rate': False,
    'learning_rate': 1e-3,
    'weight_decay': 1e-6,
    'grad_clip_thresh': 1.0,
    'batch_size': 15, #was 32
    'mask_padding': True
}


    if hparams_dict:
        hparams.update(hparams_dict)

    if verbose:
        for key, value in hparams.items():
            print(f"{key}: {value}")

    return hparams