import os
import subprocess
# Trainer: Where the ✨️ happens.
# TrainingArgs: Defines the set of arguments of the Trainer.
from TTS.trainer import Trainer, TrainingArgs

# GlowTTSConfig: all model related values for training, validating and testing.
from TTS.tts.configs.glow_tts_config import GlowTTSConfig

# BaseDatasetConfig: defines name, formatter and path of the dataset.
from TTS.tts.configs.shared_configs import BaseDatasetConfig
from TTS.tts.datasets import load_tts_samples
from TTS.tts.models.glow_tts import GlowTTS
from TTS.utils.audio import AudioProcessor
os.environ["CUDA_VISIBLE_DEVICES"]="1"

TASK="inference_model"#train_modelL

if TASK == "train_model":
    # we use the same path as this script as our training folder.
    output_path = os.path.dirname(os.path.abspath(__file__))
    print('output_path',output_path)
    # asf

    # DEFINE DATASET CONFIG
    # Set LJSpeech as our target dataset and define its path.
    # You can also use a simple Dict to define the dataset and pass it to your custom formatter.
    dataset_config = BaseDatasetConfig(
        name="ljspeech", meta_file_train="metadata.csv", path=os.path.join(output_path, "recipes/ljspeech/LJSpeech-1.1/")
    )
    # print(dataset_config)

    # INITIALIZE THE TRAINING CONFIGURATION
    # Configure the model. Every config class inherits the BaseTTSConfig.
    config = GlowTTSConfig(
        batch_size=32,
        eval_batch_size=16,
        num_loader_workers=4,
        num_eval_loader_workers=4,
        run_eval=True,
        test_delay_epochs=-1,
        epochs=1000,
        text_cleaner="phoneme_cleaners",
        use_phonemes=True,
        phoneme_language="en-us",
        phoneme_cache_path=os.path.join(output_path, "phoneme_cache"),
        print_step=25,
        print_eval=False,
        mixed_precision=True,
        output_path=output_path,
        datasets=[dataset_config],
    )
    # print(config)

    # INITIALIZE THE AUDIO PROCESSOR
    # Audio processor is used for feature extraction and audio I/O.
    # It mainly serves to the dataloader and the training loggers.
    ap = AudioProcessor(**config.audio.to_dict())

    # LOAD DATA SAMPLES
    # Each sample is a list of ```[text, audio_file_path, speaker_name]```
    # You can define your custom sample loader returning the list of samples.
    # Or define your custom formatter and pass it to the `load_tts_samples`.
    # Check `TTS.tts.datasets.load_tts_samples` for more details.
    train_samples, eval_samples = load_tts_samples(dataset_config, eval_split=True)
    # print(eval_samples[0])
    # ['A molecular change takes place in the nerve of the tentacle,\n', '/home/atseng/SCRATCH/DL/project/TTS/recipes/ljspeech/LJSpeech-1.1/wavs/LJ025-0134.wav', 'ljspeech']

    # INITIALIZE THE MODEL
    # Models take a config object and a speaker manager as input
    # Config defines the details of the model like the number of layers, the size of the embedding, etc.
    # Speaker manager is used by multi-speaker models.
    model = GlowTTS(config, speaker_manager=None)

    # INITIALIZE THE TRAINER
    # Trainer provides a generic API to train all the 🐸TTS models with all its perks like mixed-precision training,
    # distributed training, etc.
    trainer = Trainer(
        TrainingArgs(),
        config,
        output_path,
        model=model,
        train_samples=train_samples,
        eval_samples=eval_samples,
        training_assets={"audio_processor": ap},  # assets are objetcs used by the models but not class members.
    )

    # AND... 3,2,1... 🚀
    trainer.fit()
elif TASK == "inference_model":
    # print("HI")
    # /home/atseng/SCRATCH/DL/project/TTS/recipes/ljspeech/LJSpeech-1.1/wavs/LJ001-0001.wav
    # python run_predict.py --mode predict_file --pretrained_model weights/nisqa.tar --deg /path/to/wav/file.wav --output_dir /path/to/dir/with/results
    srpt='tts --text "Printing, in the only sense with which we are at present concerned, differs from most if not from all the arts and crafts represented in the Exhibition" \
      --model_path coqui_tts-November-22-2021_01+41PM-33aa27e2/best_model.pth.tar \
      --config_path coqui_tts-November-22-2021_01+41PM-33aa27e2/config.json \
      --out_path savedoutputs/output_TTS_poorq.wav'
    subprocess.call(srpt, shell=True)
elif TASK == "finetune_model":
    pass


#     CUDA_VISIBLE_DEVICES="0" python recipes/ljspeech/glow_tts/train_glowtts.py \
#     --restore_path  /home/ubuntu/.local/share/tts/tts_models--en--ljspeech--glow-tts

#     CUDA_VISIBLE_DEVICES="0" python TTS/bin/train_tts.py \
#     --config_path  /home/ubuntu/.local/share/tts/tts_models--en--ljspeech--glow-tts/config.json \
#     --restore_path  /home/ubuntu/.local/share/tts/tts_models--en--ljspeech--glow-tts

#     CUDA_VISIBLE_DEVICES="0" python recipes/ljspeech/glow_tts/train_glowtts.py \
#     --restore_path  /home/ubuntu/.local/share/tts/tts_models--en--ljspeech--glow-tts
#     --coqpit.run_name "glow-tts-finetune" \
#     --coqpit.lr 0.00001

#     # VCTK is here:
#     # /mnt/aibb_data/development/atseng/vcloning
#     # """
elif TASK == "evaluation":
    
    pass