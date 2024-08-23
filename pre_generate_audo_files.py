from gtts import gTTS
from pygame import mixer
import os
from game_data import game_steps

def generateAudoFiles(text, step=None, option=None):
    language = 'sv'
    if (option is None):
        filename = f"soundfiles/sound{step}.mp3"
    else:
        filename = f"soundfiles/sound{step}-{option}.mp3"

    soundobj = gTTS(text=text, lang=language, slow=False)
    soundobj.save(filename)


def pregenerateAllAudioFiles(game_steps):
    for step, value in game_steps.items():
        print(f"Generating audio files for {step}")
        generateAudoFiles(value['scenario'], step)
        if 'options' in value:
            print(f"Generating audio files for {step} options")
            for option, text in value['options'].items():
                generateAudoFiles(text, step, option)

if __name__ == "__main__":
    pregenerateAllAudioFiles(game_steps)