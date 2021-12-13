import subprocess
import json
import tqdm
import os
import glob
# INFfastpitch=True
# INFteco=False
# if INFfastpitch:
#     model_name = "fast_pitch"
#     model_paths=["/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/checkpoint_902700.pth.tar",
#     "/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/checkpoint_911550.pth.tar",
#     "/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/checkpoint_920400.pth.tar",
#     "/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/checkpoint_929250.pth.tar"]
#     config_path = "/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/config.json"
#     speakers_file_path ="/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/speakers.json"
# elif INFteco:
#     pass
# text_list = ["Now let us to business.",
# "What did it mean?",
# "'Uncas will stay,' was the calm reply",
# "My remark pleases him, but I soon prove to him that it is not the right way to speak, however perfect may have been the language of that ancient writer.",
# "And people paint fruit, and dead fish on platters, and pitchers of lemonade with ice in,--why don't you try things like those?",
# "The 'badauds', who never fail to congregate near the carriage of princes, no matter if they have seen them a hundred times, or if they know them to be as ugly as monkeys, repeated the words of the duchess everywhere, and that was enough to send here all the snuff-takers of the capital in a hurry."
# ]

# with open(speakers_file_path) as f:
#     spk = json.load(f)
#     # spk_id = list(spk.keys())
#     for speaker_idx in tqdm.tqdm(spk.keys()):
#         for m_id, model_path in enumerate(model_paths):
#             for t_id, text in enumerate(text_list):
#                 wav_path = "/mnt/aibb_data/development/atseng/VCproject/inference_results/{}/checkpoint_{}_text_{}_speaker_{}.wav".format(model_name,m_id,t_id,speaker_idx)
#                 # output_path = "/mnt/aibb_data/development/atseng/VCproject/inference_results/{}_eval/checkpoint_{}_text_{}_speaker_{}.csv".format(model_name,m_id,t_id,speaker_idx)
#                 output_dir = "/mnt/aibb_data/development/atseng/VCproject/inference_results/{}_eval".format(model_name)
#                 srpt='python NISQA/run_predict.py --mode predict_file --pretrained_model NISQA/weights/nisqa.tar \
#                     --deg {} --output_dir {}'.format(wav_path,output_dir)
#                 subprocess.call(srpt, shell=True)
#                 os.rename(output_dir+'/NISQA_results.csv', output_dir+'/checkpoint_{}_text_{}_speaker_{}.csv'.format(m_id,t_id,speaker_idx))

eval_fastpitch=True
eval_vits=False

if eval_fastpitch:
    model_name = "fast_pitch"
    speaker_idx = "1272"
    wav_dir = "/home/atseng/SCRATCH/DL/project/TTS/voice_samples/{}".format(model_name)
    for wav_path in glob.glob(wav_dir+"/*.wav"):
        output_dir = "voice_samples/{}/nisqa_score".format(model_name)
        srpt='python NISQA/run_predict.py --mode predict_file --pretrained_model NISQA/weights/nisqa.tar \
                    --deg {} --output_dir {}'.format(wav_path,output_dir)
        subprocess.call(srpt, shell=True)
        os.rename(output_dir+'/NISQA_results.csv', output_dir+'/epoch_100_text_{}_speaker_{}.csv'.format(wav_path.split("/")[-1].split(".")[0],speaker_idx))

elif eval_vits:
    model_name = "vits"
    speaker_idx = "1272"
    wav_dir = "/home/atseng/SCRATCH/DL/project/TTS/voice_samples/{}".format(model_name)
    for wav_path in glob.glob(wav_dir+"/*.wav"):
        output_dir = "voice_samples/{}/nisqa_score".format(model_name)
        srpt='python NISQA/run_predict.py --mode predict_file --pretrained_model NISQA/weights/nisqa.tar \
                    --deg {} --output_dir {}'.format(wav_path,output_dir)
        subprocess.call(srpt, shell=True)
        os.rename(output_dir+'/NISQA_results.csv', output_dir+'/epoch_100_text_{}_speaker_{}.csv'.format(wav_path.split("/")[-1].split(".")[0],speaker_idx))




#     .format(model_name,m_id,t_id,speaker_idx)
#                 # output_path = "/mnt/aibb_data/development/atseng/VCproject/inference_results/{}_eval/checkpoint_{}_text_{}_speaker_{}.csv".format(model_name,m_id,t_id,speaker_idx)
#                 output_dir = "/mnt/aibb_data/development/atseng/VCproject/inference_results/{}_eval".format(model_name)
#                 srpt='python NISQA/run_predict.py --mode predict_file --pretrained_model NISQA/weights/nisqa.tar \
#                     --deg {} --output_dir {}'.format(wav_path,output_dir)
#                 subprocess.call(srpt, shell=True)
#                 os.rename(output_dir+'/NISQA_results.csv', output_dir+'/checkpoint_{}_text_{}_speaker_{}.csv'.format(m_id,t_id,speaker_idx))


#     pass
# text_list = ["Now let us to business.",
# "What did it mean?",
# "'Uncas will stay,' was the calm reply",
# "My remark pleases him, but I soon prove to him that it is not the right way to speak, however perfect may have been the language of that ancient writer.",
# "And people paint fruit, and dead fish on platters, and pitchers of lemonade with ice in,--why don't you try things like those?",
# "The 'badauds', who never fail to congregate near the carriage of princes, no matter if they have seen them a hundred times, or if they know them to be as ugly as monkeys, repeated the words of the duchess everywhere, and that was enough to send here all the snuff-takers of the capital in a hurry."
# ]

# with open(speakers_file_path) as f:
#     spk = json.load(f)
#     # spk_id = list(spk.keys())
#     for speaker_idx in tqdm.tqdm(spk.keys()):
#         for m_id, model_path in enumerate(model_paths):
#             for t_id, text in enumerate(text_list):
#                 wav_path = "/mnt/aibb_data/development/atseng/VCproject/inference_results/{}/checkpoint_{}_text_{}_speaker_{}.wav".format(model_name,m_id,t_id,speaker_idx)
#                 # output_path = "/mnt/aibb_data/development/atseng/VCproject/inference_results/{}_eval/checkpoint_{}_text_{}_speaker_{}.csv".format(model_name,m_id,t_id,speaker_idx)
#                 output_dir = "/mnt/aibb_data/development/atseng/VCproject/inference_results/{}_eval".format(model_name)
#                 srpt='python NISQA/run_predict.py --mode predict_file --pretrained_model NISQA/weights/nisqa.tar \
#                     --deg {} --output_dir {}'.format(wav_path,output_dir)
#                 subprocess.call(srpt, shell=True)
#                 os.rename(output_dir+'/NISQA_results.csv', output_dir+'/checkpoint_{}_text_{}_speaker_{}.csv'.format(m_id,t_id,speaker_idx))
