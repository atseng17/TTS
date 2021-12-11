import subprocess
import json
import tqdm

# text = "Text for TTSs"
model_name = "fast_pitch"
model_paths=["/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/checkpoint_902700.pth.tar",
"/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/checkpoint_911550.pth.tar",
"/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/checkpoint_920400.pth.tar",
"/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/checkpoint_929250.pth.tar"]
config_path = "/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/config.json"
speakers_file_path ="/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/speakers.json"
text_list = ["Now let us to business.",
"What did it mean?",
"'Uncas will stay,' was the calm reply",
"My remark pleases him, but I soon prove to him that it is not the right way to speak, however perfect may have been the language of that ancient writer.",
"And people paint fruit, and dead fish on platters, and pitchers of lemonade with ice in,--why don't you try things like those?",
"The 'badauds', who never fail to congregate near the carriage of princes, no matter if they have seen them a hundred times, or if they know them to be as ugly as monkeys, repeated the words of the duchess everywhere, and that was enough to send here all the snuff-takers of the capital in a hurry."
]

with open(speakers_file_path) as f:
    spk = json.load(f)
    # spk_id = list(spk.keys())
    for speaker_idx in tqdm.tqdm(spk.keys()):
        for m_id, model_path in enumerate(model_paths):
            for t_id, text in enumerate(text_list):
                out_path = "/mnt/aibb_data/development/atseng/VCproject/inference_results/{}/checkpoint_{}_text_{}_speaker_{}.wav".format(model_name,m_id,t_id,speaker_idx)
                srpt='tts --text "{}" --out_path {} --model_path {} --config_path {} --speakers_file_path {} --speaker_idx {}'.format(text,out_path, model_path, config_path, speakers_file_path, speaker_idx)
                subprocess.call(srpt, shell=True)
