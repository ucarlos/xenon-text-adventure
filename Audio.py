# -----------------------------------------------------------------------------
# Created by Ulysses Carlos on 06/26/2020 at 03:08 PM
#
# Audio.py
# This file handles playing an audio file in audio/ depending on what
# room the character is in.
# -----------------------------------------------------------------------------

# Modules:
from pydub import AudioSegment
from pydub.playback import play


def initial_test():
    song_path = "./audio/03 Realize.m4a"
    sound = AudioSegment.from_file(song_path, "m4a")
    fade = sound.fade_out(10 * 1000)
    play(fade)


def play_song_with_options(song_path, audio_format, options):
    """
    Play an audio file located in song_path with a specified audio_format.
    Options is a dictionary type of <string : int>
    that allows fade-in (in seconds)
    fade-out (in seconds), and loop options
    """
    initial_file = AudioSegment.from_file(song_path, audio_format)
    # Apply options to initial_file:
    modified_file = initial_file
    second = 1000

    for i in options:
        if i == "fade-in":
            # Apply fade-in to file
            modified_file = modified_file.fade_in(int(options["fade-in"])
                                                  * second)
        elif i == "fade-out":
            modified_file = modified_file.fade_out(int(options["fade-out"])
                                                   * second)
        elif i == "loop":
            modified_file = modified_file * int(options["loop"])
        else:
            continue

    # Now play the file.
    play(modified_file)


def play_song(song_path, audio_format):
    """
    Play an audio file located in song path with a specified audio format.
    """
    audio_file = AudioSegment.from_file(song_path, audio_format)
    # Now play audio_file:
    play(audio_file)
