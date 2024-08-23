from colorama import Fore, Style
from itertools import cycle
import os
import sys
import subprocess
import time
from tqdm import tqdm
from gtts import gTTS
from pygame import mixer
from game_data import game_steps
import random 
import threading

class GameOver(Exception):
    pass

def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(columns)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # clear the console

ascii_art = {
    'A': ['  *  ', ' * * ', '*   *', '*****', '*   *'],
    'B': ['**** ', '*   *', '*****', '*   *', '**** '],
    'C': [' ****', '*    ', '*    ', '*    ', ' ****'],
    'D': ['**** ', '*   *', '*   *', '*   *', '**** '],
    'E': ['*****', '*    ', '*****', '*    ', '*****'],
    'F': ['*****', '*    ', '*****', '*    ', '*    '],
    'G': [' ****', '*    ', '*  **', '*   *', ' ****'],
    'H': ['*   *', '*   *', '*****', '*   *', '*   *'],
    'I': ['*****', '  *  ', '  *  ', '  *  ', '*****'],
    'J': ['*****', '   * ', '   * ', '*  * ', '**** '],
    'K': ['*   *', '* *  ', '**   ', '* *  ', '*   *'],
    'L': ['*    ', '*    ', '*    ', '*    ', '*****'],
    'M': ['*   *', '** **', '* * *', '*   *', '*   *'],
    'N': ['*   *', '**  *', '* * *', '*  **', '*   *'],
    'O': ['**** ', '*  * ', '*   *', '*  * ', '**** '],
    'P': ['*****', '*   *', '*****', '*    ', '*    '],
    'Q': ['**** ', '*  * ', '*   *', '**** ', '    *'],
    'R': ['**** ', '*   *', '**** ', '* *  ', '*   *'],
    'S': [' ****', '*    ', ' *** ', '    *', '**** '],
    'T': ['*****', '  *  ', '  *  ', '  *  ', '  *  '],
    'U': ['*   *', '*   *', '*   *', '*   *', ' *** '],
    'V': ['*   *', '*   *', ' * * ', ' * * ', '  *  '],
    'W': ['*   *', '*   *', '* * *', '** **', '*   *'],
    'X': ['*   *', ' * * ', '  *  ', ' * * ', '*   *'],
    'Y': ['*   *', ' * * ', '  *  ', '  *  ', '  *  '],
    'Z': ['*****', '   * ', '  *  ', ' *   ', '*****'],
    ' ': ['     ', '     ', '     ', '     ', '     '],
    '!': ['  *  ', '  *  ', '  *  ', '     ', '  *  '],
    }

loading_messages = {
  1: "Testar synskärpan... Spel laddas!",
  2: "Fixar brytningsindex... Spel laddas!",
  3: "Anpassar astigmatism-parametrar... Spel laddas!",
  4: "Kalibrerar ögonglasögon... Spel laddas!",
  5: "Justerar hjärnsignaler till ögonen... Spel laddas!",
  6: "Kontrollerar din synvinkel... Spel laddas!",
  7: "Korrigera perifer vision... Spel laddas!",
  8: "Justerar kontaktlinser för perfekt syn... Spel laddas!",
  9: "Prova prismaeffekt... Spel laddas!",
  10: "Stämmer av ditt synfält... Spel laddas!"
}
def print_big(text, delay=0):
    text = text.upper()
    colors = cycle([Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA])
    colorsa = cycle([Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA])
    colorsb = cycle([Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA])
    
    print()
    
    horizontal_line = "=" * 140
    for l in horizontal_line:
        print(next(colorsa) + l + Fore.RESET, end='')
    print()
    lines = [''] * 5  # 5 lines for the height of letters
    for char in text:
        for i in range(5):
            lines[i] += ascii_art[char][i] + ' '
    for line in lines:
        print(next(colors) + line + Fore.RESET)
        time.sleep(delay)  # delay for "animation"
    for l in horizontal_line:
        print(next(colorsa) + l + Fore.RESET, end='')
    print()
    print()

def slowPrint(string, speed=0.005):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)



def game(step, currentStep=0):
    slowPrint(Fore.BLUE + step['scenario'] + Fore.RESET, 0)

    readOutLoud(step['scenario'], currentStep)  # Read out the scenario

    if 'completed' in step and step['completed'] is not None:
        print('')
        ending_message_1 = "Du introducerar dig själv och hon ler välkomnande. Ni börjar prata och blir snart goda vänner. Dagarna går och ni lever tillsammans på marken som tillhör Vänneböke 2279, ni hjälps åt att odla grönsaker, tar hand om huset och njuter av varandras sällskap."
        print(Fore.RED + ending_message_1 + Fore.RESET)
        readOutLoud(ending_message_1, uniqueName='ending_message_1')
        print('')
        ending_message_2 =  "Eran kärlek växer för varje dag som går och efter några år föds Leonora. Grattis du vann spelet och livet!"
        print(Fore.RED + ending_message_2 + Fore.RESET)
        readOutLoud(ending_message_2, uniqueName='ending_message_2')
        print('')
        print(Fore.RED + "" + Fore.RESET)
        print('')
        print_big('VICTORS ADVENTURE ')
        return
    for i, (option, text) in enumerate(step['options'].items(), start=1):
        print('')
        print(f"{Fore.GREEN}{option}) {text}{Fore.RESET}")
        readOutLoud(text, currentStep, option)  # Read out the options

    print('')
    choice = input(Fore.YELLOW + "Ditt val: " + Fore.RESET)
    if choice not in step['next']:
        print('Invalid choice. reseting ...\n')
        time.sleep(1)
        clear_screen()
        print_big('   VICTORS ADVENTURE   ', 0.1)
        game(step, currentStep)
    else:
        next_step = step['next'][choice]
        if next_step == 'gameover':
            subprocess.Popen(["afplay", "soundfiles/gameover.wav"]) 
            print(Fore.RED + step['gameover'] + Fore.RESET)
            print('')
            raise GameOver
        else:
            subprocess.Popen(["afplay", "soundfiles/level_up.mp3"]) 
            clear_screen()
            print_big('   VICTORS ADVENTURE   ')
            game(game_steps[next_step], next_step)

# This function generates an audio file from the given text using Google Text-to-Speech (gTTS) library.
# The function first checks if the audio file for specific step already exists or not.
# If the audio file does not exist, it will generate a new audio file.
# If the file already exists, it will use the existing file instead of creating a new one.
# Finally, it plays the audio file using pygame's mixer.
def readOutLoud(text, step=None, option=None, uniqueName=None):
    language = 'sv'  # Swedish language
    if(uniqueName is not None):
        filename = f"soundfiles/{uniqueName}.mp3"
    else:
        if (option is None):
            filename = f"soundfiles/sound{step}.mp3"
        else:
            filename = f"soundfiles/sound{step}-{option}.mp3"
    

    # Check if file already exists
    if not os.path.isfile(filename):
        soundobj = gTTS(text=text, lang=language, slow=False)
        soundobj.save(filename)

    # Load and play existing file
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    while mixer.music.get_busy():
        continue

def loading():
    animation = "|/-\\"
    start_time = time.time()
    print(random.choice(list(loading_messages.values())))
    while True:
        for i in range(4):
            time.sleep(0.2)  # Feel free to experiment with the speed here
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        if time.time() - start_time > 4:  # The animation will last for 10 seconds
            break
def main():
    subprocess.Popen(["afplay", "soundfiles/start_sound.mp3"]) 
    mixer.init()
    clear_screen()
    print_big('   VICTORS ADVENTURE   ', 0.4)
    loading_thread = threading.Thread(target=loading)
    loading_thread.start()
    loading_thread.join()

    clear_screen()
    print_big('   READY ', 0)
    time.sleep(0.4)
    clear_screen()
    print_big('         SET', 0)
    time.sleep(0.4)
    clear_screen()
    print_big('               GO!!!!', 0)
    time.sleep(0.6)
    clear_screen()
    
    print_big('   VICTORS ADVENTURE   ', 0)
    try:
        game(game_steps[1], 1)
    except GameOver:
        slowPrint("\nGame Over. Ta en klunk ur din dricka. Börja om? Y/N:")
        if input().lower() == 'y':
            main()
if __name__ == "__main__":
    main()
    # Facit till spelet: 