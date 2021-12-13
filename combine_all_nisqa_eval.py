import subprocess
import json
import tqdm
import os
import glob
import pandas as pd
ept_ls = []
short_score = []
short_score = []
short_score = []
long_score = []
long_question_score = []
long_score = []
score_dict = dict()
model_name = "fast_pitch"
model_name = "vits"

for n_f in glob.glob("/home/atseng/SCRATCH/DL/project/TTS/voice_samples_additional/{}/nisqa_score/*.csv".format(model_name)):
    f_name = n_f.split("/")[-1].split(".")[0][:-10]
    scores = pd.read_csv(n_f).values[0][1:-1]
    if f_name[:-2] not in score_dict:
        score_dict[f_name[:-2]] = scores
    else:
        score_dict[f_name[:-2]] += scores
    # if f_name[:-2]=""
    # print(f_name[:-2])
#     df_tmp = pd.read_csv(n_f)
#     df_tmp.values[0][1:-1]
#     ept_ls.append(list(df_tmp.values[0][1:-1]))
for key,val in score_dict.items():
    score_dict[key] =  val/6
print(score_dict)
    


# INFfastpitch=True
# # INFteco=True
# syn_output_name = ["short","short_question","short_tough_word","long","long_question","long_tough_word"]
# # short
# short_list = ["Now let us to business.",
# "Don't begin!",
# "I suppose so.",
# "I know you.",
# "That's right."]
# # short question
# short_question_list = ["What did it mean?",
# "Are you the cashier?",
# "Am I in bed?",
# "How do you do?",
# "What is that in your hand?"]
# # short tough word
# short_tough_word_list = ["'Uncas will stay,' was the calm reply",
# "'Yes, indeed,' Cresswell agreed.",
# "'Bless me!' said Mr. Beale uncomfortably.",
# "'It's better'n Fiff of November,' said Dickie; 'and I do like you.'",
# "And after that Sigurd was called Fafnir's Bane, and Dragonslayer."]
# # long
# long_list = ["My remark pleases him, but I soon prove to him that it is not the right way to speak, however perfect may have been the language of that ancient writer.",
# "But though he rubbed his eyes and did everything he could to keep himself awake it was all in vain, for the Bushy Bride crooned and sang till his eyes were fast closed, and when the beautiful young maiden came he was sound asleep and snoring.",
# "Very much of squalor and discomfort will be endured before the last trinket or the last pretense of pecuniary decency is put away."
# "And so life and death have dispersed the circle of 'violent Radicals and Dissenters' into which, twenty years ago, the little, quiet, resolute clergyman's daughter was received, and by whom she was truly loved and honoured.",
# "The people contested these measures one by one in the courts; presenting in case after case the different phases of the subject, and urging the unconstitutionality of the measure."]
# # long question
# long_question_list = ["And people paint fruit, and dead fish on platters, and pitchers of lemonade with ice in,--why don't you try things like those?",
# "'Have you any band instruments of an easy nature to play?' demanded the Chief Organiser of the Prison Governor; 'drums, cymbals, those sort of things?'",
# "Ruth asked the enthusiasts if they would like to live in such a sounding mausoleum, with its great halls and echoing rooms, and no comfortable place in it for the accommodation of any body?",
# "And people paint fruit, and dead fish on platters, and pitchers of lemonade with ice in,--why don't you try things like those?",
# "Words can not express the strength of my devotion, but for that very reason I must do what duty commands before I ask the question, 'Will you join your fate to mine?"]
# # long tough word
# long_tough_word_list = ["The 'badauds', who never fail to congregate near the carriage of princes, no matter if they have seen them a hundred times, or if they know them to be as ugly as monkeys, repeated the words of the duchess everywhere, and that was enough to send here all the snuff-takers of the capital in a hurry.",
# "Suddenly the ichthyosaurus and the plesiosaurus disappear below, leaving a whirlpool eddying in the water.",
# "Now Brynhild had no help but to promise she would be his wife, the wife of Gunnar as she supposed, for Sigurd wore Gunnar's shape, and she had sworn to wed whoever should ride the flames.",
# "American school boys read with emotions of horror of the Albigenses, driven, beaten and killed, with a papal legate directing the butchery; and of the Vaudois, hunted and hounded like beasts as the effect of a royal decree; and they yet shall read in the history of their own country of scenes as terrible as these in the exhibition of injustice and inhuman hate.",
# "Then for the three years before her mother's death there had been surreptitious lessons from a Portland teacher, paid for out of Mr. Lord's house allowance; for one of his chief faults was an incredible parsimony, amounting almost to miserliness."]

# if INFfastpitch:
#     model_name = "fast_pitch"
#     model_paths=["/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/checkpoint_929250.pth.tar"]
#     config_path = "/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/config.json"
#     speakers_file_path ="/mnt/aibb_data/development/atseng/VCproject/trained_models/fast_pitch/fast_pitch_ljspeech-December-09-2021_08+25PM-f92878cf/speakers.json"
# else:
#     pass
# with open(speakers_file_path) as f:
#     spk = json.load(f)
#     for speaker_idx in tqdm.tqdm(spk.keys()):
#         if speaker_idx=="LTTS_1272":
#             for m_id, model_path in enumerate(model_paths):
#                 for cat_id, text_list in enumerate([short_list,short_question_list,short_tough_word_list,long_list,long_question_list,long_tough_word_list]):
#                     for t_id, text in enumerate(text_list):
#                         syn_output_path = "voice_samples_additional/fast_pitch/{}_{}_{}.wav".format(syn_output_name[cat_id],t_id,speaker_idx)
#                         srpt='tts --text "{}" --out_path {} --model_path {} --config_path {} --speakers_file_path {} --speaker_idx {}'.format(text,syn_output_path, model_path, config_path, speakers_file_path, speaker_idx)
#                         subprocess.call(srpt, shell=True)
                        
#                         nisqa_output_dir = "voice_samples_additional/{}/nisqa_score".format(model_name)
#                         srpt='python NISQA/run_predict.py --mode predict_file --pretrained_model NISQA/weights/nisqa.tar \
#                                     --deg {} --output_dir {}'.format(syn_output_path,nisqa_output_dir)
#                         subprocess.call(srpt, shell=True)
#                         os.rename(nisqa_output_dir+'/NISQA_results.csv', nisqa_output_dir+'/{}.csv'.format(syn_output_path.split("/")[-1].split(".")[0]))
#         else:
#             pass
