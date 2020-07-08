# -----------------------------------------------------------------------------
# Created by Ulysses Carlos on 07/02/2020 at 09:34 PM
#
# Simple_Audio.py
# Simple audio playback using playsound.
# -----------------------------------------------------------------------------
from playsound import playsound

def play_song(file_path):
    """
    Play an audio file located in file_path using playsound.
    """
    playsound(file_path)
