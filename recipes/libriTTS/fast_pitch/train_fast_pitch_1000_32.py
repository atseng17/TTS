import os

from TTS.config import BaseAudioConfig, BaseDatasetConfig
from TTS.trainer import Trainer, TrainingArgs
from TTS.tts.configs.fast_pitch_config import FastPitchConfig
from TTS.tts.datasets import load_tts_samples
from TTS.tts.models.forward_tts import ForwardTTS
from TTS.tts.utils.speakers import SpeakerManager
from TTS.utils.audio import AudioProcessor

# output_path = os.path.dirname(os.path.abspath(__file__))
output_path = "/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch"
# dataset_config = BaseDatasetConfig(name="vctk", meta_file_train="", path=os.path.join(output_path, "../VCTK/"))

dataset_path = "/mnt/aibb_data/development/atseng/VCproject/LibriTTS/dev-clean"
dataset_config = BaseDatasetConfig(name="libri_tts", meta_file_train=None, path=dataset_path)

audio_config = BaseAudioConfig(
    sample_rate=22050,
    do_trim_silence=True,
    trim_db=23.0,
    signal_norm=False,
    mel_fmin=0.0,
    mel_fmax=8000,
    spec_gain=1.0,
    log_func="np.log",
    ref_level_db=20,
    preemphasis=0.0,
)

config = FastPitchConfig(
    run_name="fast_pitch_ljspeech",
    audio=audio_config,
    batch_size=16,
    eval_batch_size=16,
    num_loader_workers=8,
    num_eval_loader_workers=4,
    compute_input_seq_cache=True,
    compute_f0=True,
    f0_cache_path=os.path.join(output_path, "f0_cache"),
    run_eval=True,
    test_delay_epochs=-1,
    epochs=100,
    text_cleaner="english_cleaners",
    use_phonemes=True,
    use_espeak_phonemes=False,
    phoneme_language="en-us",
    phoneme_cache_path=os.path.join(output_path, "phoneme_cache"),
    print_step=50,
    print_eval=False,
    mixed_precision=False,
    sort_by_audio_len=True,
    max_seq_len=500000,
    output_path=output_path,
    datasets=[dataset_config],
    use_speaker_embedding=True,
)
print(config.save_step)
# sdfsf
config.audio.sample_rate = 24000
config.save_step = 8850

print("config.save_step:",config.save_step)
# init audio processor
ap = AudioProcessor(**config.audio)

# load training samples
train_samples, eval_samples = load_tts_samples(dataset_config, eval_split=True)
print("how many steps in a epoch:",len(train_samples)/config.batch_size)
# sdfs
# init speaker manager for multi-speaker training
# it maps speaker-id to speaker-name in the model and data-loader
speaker_manager = SpeakerManager()
speaker_manager.set_speaker_ids_from_data(train_samples + eval_samples)
config.model_args.num_speakers = speaker_manager.num_speakers

# init model
model = ForwardTTS(config, speaker_manager)

# init the trainer and 🚀
trainer = Trainer(
    TrainingArgs(),
    config,
    output_path,
    model=model,
    train_samples=train_samples,
    eval_samples=eval_samples,
    training_assets={"audio_processor": ap},
)
trainer.fit()
