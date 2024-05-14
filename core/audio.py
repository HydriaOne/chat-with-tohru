import time
from pygame import mixer

def play_file(path_to_file):
    mixer.init()
    mixer.music.load(path_to_file)
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)
