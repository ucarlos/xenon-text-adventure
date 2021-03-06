# -----------------------------------------------------------------------------
# Created by Ulysses Carlos on 06/26/2020 at 04:47 PM
#
# Main.py
# This is the main file for the project that handles creating threads
# that handle audio and playback.
# -----------------------------------------------------------------------------
import threading
# import Simple_Audio
import Engine

from pathlib import Path
from pathlib import PurePath
from os import fspath

# Variable that handles killing the audio thread.

# KILL_AUDIO_THREAD = False


# def audio_thread(file_path):
#     """
#     Play an audio file located in file_path repeatedly until the
#     KILL_AUDIO_THREAD is toggled on.
#     """

#     # Create a file that audio will write to.

#     # print("This thread handles the audio portion of the program.")
#     # audio_file = "./audio/06 Access.m4a"

#     while not KILL_AUDIO_THREAD:
#         # song = Simple_Audio.play_song(file_path)
#         play_song(file_path, "mp3")
#         # del song
        


# def test_input_thread():
#     print("This thread handles the input portion of the program.")
#     print("For example, please type something. (Quit by writing 'quit')")

#     user_input = input()
#     user_input.lower()
#     while user_input != 'quit':
#         print(f"You wrote {user_input}")
#         user_input = input()
#         user_input.lower()

#     if user_input == "quit":
#         global KILL_AUDIO_THREAD
#         KILL_AUDIO_THREAD = True


# def test():
#     # Create a Pysch Room Scene:
#     # temp = Scene.ApartmentRoomScene()
#     temp = Engine.Scene.CryrogenicRoomScene()
#     temp.enter_scene()

#     global KILL_AUDIO_THREAD
#     KILL_AUDIO_THREAD = True


def start_engine():
    game = Engine.Engine()
    game.start_game()


def main():
    """
    Handles creating threads for playing sound and handling the engine.
    """
    # print("Starting the program...")
    # print("Creating Audio thread...")
    # audio_directory = Path.cwd() / "audio"
    # audio_directory = PurePath(audio_directory)
    # file_path = audio_directory / "07 Access.mp3"

    # Now convert to file:
    # file_path = reconstruct_file_path(file_path)
    # print(file_path)
    # file_path = "./audio/07 Access.ogg"
    # audio_t = threading.Thread(target=audio_thread, args=[file_path])
    # print("Creating Input thread...")
    # input_t = threading.Thread(target=start_engine)

    # print("Executing Audio thread...")
    # audio_t.start()

    # print("Executing Input thread...")
    # input_t.start()
    start_engine()


# Execute the program:
main()
