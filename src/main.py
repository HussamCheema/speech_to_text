import vlc
import sys
sys.path.append("../")

from utils.io import *
import sys


if __name__ == "__main__":
    # pipeline = Pipeline()
    # pipeline.start()

    # Reading mp3 file
    signal, sr = read_mp3("/mnt/c/Users/Hussain/Desktop/project1/main/data/friends1.mp3")
    p = vlc.MediaPlayer("/mnt/c/Users/Hussain/Desktop/project1/main/data/friends1.mp3")
    p.play()
    print("owwwwwww")