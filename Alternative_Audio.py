# -----------------------------------------------------------------------------
# Created by Ulysses Carlos on 07/02/2020 at 09:34 PM
#
# Alternative_Audio.py
# Simple audio playback using playsound.
# -----------------------------------------------------------------------------
import playsound

def play_song(file_path):
    """
    Play am audio file located in file_path using playsound.
    I currently don't know if it supports m4a files, but I'll try.
    """
    playsound(file_path, 0)
