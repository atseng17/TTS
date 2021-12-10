# <img src="https://raw.githubusercontent.com/coqui-ai/TTS/main/images/coqui-log-green-TTS.png" height="56"/>

🐸TTS is a library for advanced Text-to-Speech generation. It's built on the latest research, was designed to achieve the best trade-off among ease-of-training, speed and quality.
🐸TTS comes with [pretrained models](https://github.com/coqui-ai/TTS/wiki/Released-Models), tools for measuring dataset quality and already used in **20+ languages** for products and research projects.

[![GithubActions](https://github.com/coqui-ai/TTS/actions/workflows/main.yml/badge.svg)](https://github.com/coqui-ai/TTS/actions)
[![PyPI version](https://badge.fury.io/py/TTS.svg)](https://badge.fury.io/py/TTS)
[![Covenant](https://camo.githubusercontent.com/7d620efaa3eac1c5b060ece5d6aacfcc8b81a74a04d05cd0398689c01c4463bb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6e7472696275746f72253230436f76656e616e742d76322e3025323061646f707465642d6666363962342e737667)](https://github.com/coqui-ai/TTS/blob/master/CODE_OF_CONDUCT.md)
[![Downloads](https://pepy.tech/badge/tts)](https://pepy.tech/project/tts)
[![DOI](https://zenodo.org/badge/265612440.svg)](https://zenodo.org/badge/latestdoi/265612440)

[![Docs](<https://readthedocs.org/projects/tts/badge/?version=latest&style=plastic>)](https://tts.readthedocs.io/en/latest/)
[![Gitter](https://badges.gitter.im/coqui-ai/TTS.svg)](https://gitter.im/coqui-ai/TTS?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![License](<https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg>)](https://opensource.org/licenses/MPL-2.0)

📰 [**Subscribe to 🐸Coqui.ai Newsletter**](https://coqui.ai/?subscription=true)

📢 [English Voice Samples](https://erogol.github.io/ddc-samples/) and [SoundCloud playlist](https://soundcloud.com/user-565970875/pocket-article-wavernn-and-tacotron2)

📄 [Text-to-Speech paper collection](https://github.com/erogol/TTS-papers)

<img src="https://static.scarf.sh/a.png?x-pxid=cf317fe7-2188-4721-bc01-124bb5d5dbb2" />

## 💬 Where to ask questions
Please use our dedicated channels for questions and discussion. Help is much more valuable if it's shared publicly so that more people can benefit from it.

| Type                            | Platforms                               |
| ------------------------------- | --------------------------------------- |
| 🚨 **Bug Reports**              | [GitHub Issue Tracker]                  |
| 🎁 **Feature Requests & Ideas** | [GitHub Issue Tracker]                  |
| 👩‍💻 **Usage Questions**          | [Github Discussions]                    |
| 🗯 **General Discussion**       | [Github Discussions] or [Gitter Room]   |

[github issue tracker]: https://github.com/coqui-ai/tts/issues
[github discussions]: https://github.com/coqui-ai/TTS/discussions
[gitter room]: https://gitter.im/coqui-ai/TTS?utm_source=share-link&utm_medium=link&utm_campaign=share-link
[Tutorials and Examples]: https://github.com/coqui-ai/TTS/wiki/TTS-Notebooks-and-Tutorials


## 🔗 Links and Resources
| Type                            | Links                               |
| ------------------------------- | --------------------------------------- |
| 💼 **Documentation**              | [ReadTheDocs](https://tts.readthedocs.io/en/latest/)
| 💾 **Installation**               | [TTS/README.md](https://github.com/coqui-ai/TTS/tree/dev#install-tts)|
| 👩‍💻 **Contributing**               | [CONTRIBUTING.md](https://github.com/coqui-ai/TTS/blob/main/CONTRIBUTING.md)|
| 📌 **Road Map**                   | [Main Development Plans](https://github.com/coqui-ai/TTS/issues/378)
| 🚀 **Released Models**            | [TTS Releases](https://github.com/coqui-ai/TTS/releases) and [Experimental Models](https://github.com/coqui-ai/TTS/wiki/Experimental-Released-Models)|

## 🥇 TTS Performance
<p align="center"><img src="https://raw.githubusercontent.com/coqui-ai/TTS/main/images/TTS-performance.png" width="800" /></p>

Underlined "TTS*" and "Judy*" are 🐸TTS models
<!-- [Details...](https://github.com/coqui-ai/TTS/wiki/Mean-Opinion-Score-Results) -->

## Features
- High-performance Deep Learning models for Text2Speech tasks.
    - Text2Spec models (Tacotron, Tacotron2, Glow-TTS, SpeedySpeech).
    - Speaker Encoder to compute speaker embeddings efficiently.
    - Vocoder models (MelGAN, Multiband-MelGAN, GAN-TTS, ParallelWaveGAN, WaveGrad, WaveRNN)
- Fast and efficient model training.
- Detailed training logs on the terminal and Tensorboard.
- Support for Multi-speaker TTS.
- Efficient, flexible, lightweight but feature complete `Trainer API`.
- Ability to convert PyTorch models to Tensorflow 2.0 and TFLite for inference.
- Released and read-to-use models.
- Tools to curate Text2Speech datasets under```dataset_analysis```.
- Utilities to use and test your models.
- Modular (but not too much) code base enabling easy implementation of new ideas.

## Implemented Models
### Text-to-Spectrogram
- Tacotron: [paper](https://arxiv.org/abs/1703.10135)
- Tacotron2: [paper](https://arxiv.org/abs/1712.05884)
- Glow-TTS: [paper](https://arxiv.org/abs/2005.11129)
- Speedy-Speech: [paper](https://arxiv.org/abs/2008.03802)
- Align-TTS: [paper](https://arxiv.org/abs/2003.01950)
- FastPitch: [paper](https://arxiv.org/pdf/2006.06873.pdf)
- FastSpeech: [paper](https://arxiv.org/abs/1905.09263)

### End-to-End Models
- VITS: [paper](https://arxiv.org/pdf/2106.06103)

### Attention Methods
- Guided Attention: [paper](https://arxiv.org/abs/1710.08969)
- Forward Backward Decoding: [paper](https://arxiv.org/abs/1907.09006)
- Graves Attention: [paper](https://arxiv.org/abs/1910.10288)
- Double Decoder Consistency: [blog](https://erogol.com/solving-attention-problems-of-tts-models-with-double-decoder-consistency/)
- Dynamic Convolutional Attention: [paper](https://arxiv.org/pdf/1910.10288.pdf)
- Alignment Network: [paper](https://arxiv.org/abs/2108.10447)

### Speaker Encoder
- GE2E: [paper](https://arxiv.org/abs/1710.10467)
- Angular Loss: [paper](https://arxiv.org/pdf/2003.11982.pdf)

### Vocoders
- MelGAN: [paper](https://arxiv.org/abs/1910.06711)
- MultiBandMelGAN: [paper](https://arxiv.org/abs/2005.05106)
- ParallelWaveGAN: [paper](https://arxiv.org/abs/1910.11480)
- GAN-TTS discriminators: [paper](https://arxiv.org/abs/1909.11646)
- WaveRNN: [origin](https://github.com/fatchord/WaveRNN/)
- WaveGrad: [paper](https://arxiv.org/abs/2009.00713)
- HiFiGAN: [paper](https://arxiv.org/abs/2010.05646)
- UnivNet: [paper](https://arxiv.org/abs/2106.07889)

You can also help us implement more models.

## Install TTS
🐸TTS is tested on Ubuntu 18.04 with **python >= 3.6, < 3.9**.

If you are only interested in [synthesizing speech](https://tts.readthedocs.io/en/latest/inference.html) with the released 🐸TTS models, installing from PyPI is the easiest option.

```bash
pip install TTS
```

By default, this only installs the requirements for PyTorch. To install the tensorflow dependencies as well, use the `tf` extra.

```bash
pip install TTS[tf]
```

If you plan to code or train models, clone 🐸TTS and install it locally.

```bash
git clone https://github.com/coqui-ai/TTS
pip install -e .[all,dev,notebooks,tf]  # Select the relevant extras
```

If you are on Ubuntu (Debian), you can also run following commands for installation.

```bash
$ make system-deps  # intended to be used on Ubuntu (Debian). Let us know if you have a diffent OS.
$ make install
```

If you are on Windows, 👑@GuyPaddock wrote installation instructions [here](https://stackoverflow.com/questions/66726331/how-can-i-run-mozilla-tts-coqui-tts-training-with-cuda-on-a-windows-system).

## Directory Structure
```
|- notebooks/       (Jupyter Notebooks for model evaluation, parameter selection and data analysis.)
|- utils/           (common utilities.)
|- TTS
    |- bin/             (folder for all the executables.)
      |- train*.py                  (train your target model.)
      |- distribute.py              (train your TTS model using Multiple GPUs.)
      |- compute_statistics.py      (compute dataset statistics for normalization.)
      |- convert*.py                (convert target torch model to TF.)
      |- ...
    |- tts/             (text to speech models)
        |- layers/          (model layer definitions)
        |- models/          (model definitions)
        |- tf/              (Tensorflow 2 utilities and model implementations)
        |- utils/           (model specific utilities.)
    |- speaker_encoder/ (Speaker Encoder models.)
        |- (same)
    |- vocoder/         (Vocoder models.)
        |- (same)
```


## Andrew's modifications
Training, inference, and evaluatiion of single speaker TTS
```
python andrew_playground.py
```
Training of multi speaker TTS
```
# libriTTS
python recipes/libriTTS/glow_tts/train_glow_tts_quick.py 

tts --text "Text for TTSs" --out_path savedoutputs/libris_from_scratch.wav --model_path recipes/libriTTS/glow_tts/coqui_tts-December-05-2021_10+30PM-267d77c7/best_model.pth.tar --config_path recipes/libriTTS/glow_tts/coqui_tts-December-05-2021_10+30PM-267d77c7/config.json --speakers_file_path recipes/libriTTS/glow_tts/coqui_tts-December-05-2021_10+30PM-267d77c7/speakers.json --speaker_idx LTTS_1272

# vctk
python recipes/vctk/glow_tts/train_glow_tts_quick.py



```

Inference pretrained multispeaker TT
```
tts --text "Text for TTS." --out_path savedoutputs/inf_from_pretriined_multi_TTS.wav --model_name tts_models/en/vctk/sc-glow-tts  --speaker_idx p225
```
Inference trained multispeaker TT
```

```

Fine tuning multispeaker TTS from vctk to libriTTS
```
# Fine tuning on glowtts
tts --model_name tts_models/en/vctk/sc-glow-tts --text "hello world." --speaker_wav 28.wav

CUDA_VISIBLE_DEVICES="0" python recipes/libriTTS/glow_tts/train_glow_tts.py \
    --restore_path /home/atseng/.local/share/tts/tts_models--en--vctk--sc-glow-tts/model_file.pth.tar


# Fine tuning on vits
tts --model_name tts_models/en/vctk/vits --text "hello world." --speaker_wav 28.wav

CUDA_VISIBLE_DEVICES="0" python recipes/libriTTS/vits/train_vits.py \
    --restore_path /home/atseng/.local/share/tts/tts_models--en--vctk--vits/model_file.pth.tar

# Fine tuning on TecotronDDC
tts --model_name tts_models/en/sam/tacotron-DDC --text "hello world."
<!-- CUDA_VISIBLE_DEVICES="0" python recipes/libriTTS/tacotron-DDC/train_tacotron-DDC_100_16.py \
    --restore_path /home/atseng/.local/share/tts/tts_models--en--sam--tacotron-DDC/model_file.pth.tar -->

CUDA_VISIBLE_DEVICES="0,1,2,3" python TTS/bin/distribute.py --script recipes/libriTTS/tacotron-DDC/train_tacotron-DDC_100_16.py \
    --restore_path /home/atseng/.local/share/tts/tts_models--en--sam--tacotron-DDC/model_file.pth.tar

# Fine tuning on fast pitch
tts --model_name tts_models/en/vctk/fast_pitch --text "hello world."
CUDA_VISIBLE_DEVICES="0" python recipes/libriTTS/fast_pitch/train_fast_pitch_1000_32.py \
    --restore_path /home/atseng/.local/share/tts/tts_models--en--vctk--fast_pitch/model_file.pth.tar

<!-- CUDA_VISIBLE_DEVICES="0,1,2,3" python TTS/bin/distribute.py --script recipes/libriTTS/fast_pitch/train_fast_pitch.py \
    --restore_path /home/atseng/.local/share/tts/tts_models--en--vctk--fast_pitch/model_file.pth.tar -->

```
Inference Finetuned multispeaker TTS, need fix, including https://github.com/coqui-ai/TTS/issues/932
```

# inference on glowtts
./TTS/bin/synthesize.py --text "Text for TTSs" --out_path savedoutputs/speech.wav --model_path /home/atseng/SCRATCH/DL/project/TTS/recipes/libriTTS/glow_tts/coqui_tts-December-07-2021_07+25PM-2ebd3bbd/checkpoint_90000.pth.tar --config_path /home/atseng/SCRATCH/DL/project/TTS/recipes/libriTTS/glow_tts/coqui_tts-December-07-2021_07+25PM-2ebd3bbd/config.json --speakers_file_path /home/atseng/SCRATCH/DL/project/TTS/recipes/libriTTS/glow_tts/coqui_tts-December-07-2021_07+25PM-2ebd3bbd/speakers.json --speaker_idx LTTS_1272

# inference on vits
./TTS/bin/synthesize.py --text "Text for TTSs" --out_path savedoutputs/speech.wav --model_path /home/atseng/SCRATCH/DL/project/TTS/recipes/libriTTS/vits/vits_vctk-December-07-2021_04+19PM-2ebd3bbd/best_model_1000162.pth.tar --config_path /home/atseng/SCRATCH/DL/project/TTS/recipes/libriTTS/vits/vits_vctk-December-07-2021_04+19PM-2ebd3bbd/config.json --speakers_file_path /home/atseng/SCRATCH/DL/project/TTS/recipes/libriTTS/vits/vits_vctk-December-07-2021_04+19PM-2ebd3bbd/speakers.json --speaker_idx LTTS_1272

# inference on TDDC
./TTS/bin/synthesize.py --text "Text for TTSs" --out_path savedoutputs/speech.wav --model_path recipes/libriTTS/tacotron-DDC/coqui_tts-December-07-2021_09+17PM-2ebd3bbd/checkpoint_270000.pth.tar --config_path recipes/libriTTS/tacotron-DDC/coqui_tts-December-07-2021_09+17PM-2ebd3bbd/config.json --speakers_file_path recipes/libriTTS/tacotron-DDC/coqui_tts-December-07-2021_09+17PM-2ebd3bbd/speakers.json --speaker_idx LTTS_1272


## Andrew's updates
11.23.2021 Added NISQA for speaker naturalness evaluation
11.29.2021 Added training script for training Glow-TTS on LibriTTS
12.03.2021 Added Finetuning script for SC-Glow-TTS on LibriTTS (need fix)
12.03.2021 Added Finetuning script for vits/Tacotron-DDC on LibriTTS
## Andrew's TODO's
- Speaker embedding analysis on TTS models
- Find another evaluation method for TTSs
- Figure out training log information

