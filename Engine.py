
# -----------------------------------------------------------------------------
# Created by Ulysses Carlos on 07/07/2020 at 10:10 PM
#
# Engine.py
# Contains the classes needed to run the text portion of the game.
# -----------------------------------------------------------------------------

import Scene
from Clear import clear_screen
from os import system
from os import fspath
import threading
import multiprocessing
from pathlib import Path
from pathlib import PurePath
import Pydub_Audio
# Global Variables:
audio_dir = PurePath(Path.cwd() / "audio")
AUDIO_FILE_SHOULD_LOOP = True

# ------------------------------------------------------------------------------
# Audio Thread:
# ------------------------------------------------------------------------------


def play_audio_from_scene(audio_key, audio_path):
    """
    Given a room and an audio key, play the audio file for the current scene.
    """
    # audio_key = room.get_audio_key_from_flag()

    if (audio_key == "nil" or audio_key == "" or audio_path is None):
        return
    else:
        # self.audio_file_should_loop = True
        global AUDIO_FILE_SHOULD_LOOP
        AUDIO_FILE_SHOULD_LOOP = True
        audio_path = reconstruct_file_path(audio_path)

        while AUDIO_FILE_SHOULD_LOOP:
            Pydub_Audio.play_song(audio_path, "mp3")
        return


def reconstruct_file_path(pure_path_file):
    """
    Convert a PurePath object into a valid string
    that can be read by playsound.
    """
    return fspath(pure_path_file)


class Engine(object):
    # default loop option
    audio_file_should_loop = True

    room_list = {"main-menu": Scene.MainMenuScene(),
                 "intro": Scene.OpeningRoomScene(),
                 "psychologist": Scene.PyschRoomScene(),
                 "apartment": Scene.ApartmentRoomScene(),
                 "xenon-hospital": Scene.HospitalRoomScene(),
                 "xenon-leftcorridor": Scene.LeftCorridorScene(),
                 "xenon-rightcorridor": Scene.RightCorridorScene(),
                 "xenon-observatory": Scene.ObservatoryRoomScene(),
                 "xenon-cryogenic": Scene.CryrogenicRoomScene(),
                 "save-point": Scene.SaveRoomScene(),
                 "end": Scene.EndRoomScene()}

    audio_list = {"dream": audio_dir / "03 Dream.mp3",
                  "realize": audio_dir / "04 Realize.mp3",
                  "ranphar1": audio_dir / "05 Ranphar 1.mp3",
                  "encoder": audio_dir / "06 Encoder.mp3",
                  "access": audio_dir / "07 Access.mp3",
                  "moonlight": audio_dir / "08 Moonlight.mp3",
                  "memory": audio_dir / "09 Memory.mp3",
                  "contact": audio_dir / "10 Contact.mp3",
                  "7th": audio_dir / "11 7th.mp3",
                  "fact": audio_dir / "15 Fact.mp3",
                  "past": audio_dir / "16 Past.mp3",
                  "apartment": audio_dir / "apartment.mp3"
                  }
    # Handles the audio thread.
    process_list = []
    def __init__(self):
        # Set the first and last rooms for the game
        self.first_room = self.room_list["main-menu"]
        self.last_room = self.room_list["end"]


    def start_game(self):
        # First, set the current room to first room:
        current_room = self.first_room
        current_room_audio_key = current_room.get_audio_key_from_flag()

        while current_room != self.last_room:
            next_room_name = current_room.enter_scene()
            
            if next_room_name == "end":
                break
            
            # Clear the screen.
            clear_screen()
            # Find the room with that name and continue.
            next_room = self.room_list[next_room_name]
            next_room_audio_key = next_room.get_audio_key_from_flag()

            # Change the song depending on the scene.
            # if current_room_audio_key != next_room_audio_key:
            #     # Unfortunately wait for the song to finish.
            #     # self.audio_file_should_loop = False
            #     # self.play_audio_from_scene(next_room_audio_key)
            #     if len(self.process_list) != 0:
            #         self.process_list[0].terminate()
                
            #     if next_room_audio_key == "nil" or next_room_audio_key == "":
            #         pass
            #     else:
            #         audio_path = self.audio_list[next_room_audio_key]
            #         audio_process = multiprocessing.Process(target=play_audio_from_scene,
            #                                                 args=(next_room_audio_key,
            #                                                       audio_path)
            #                                                 )
            #         audio_process.start()
            #         self.process_list.append(audio_process)               
            # Now set the current room:
            current_room = next_room
            current_room_audio_key = next_room_audio_key

        # End the game on end-room:
        # close any audio threads and end the game.
        # TODO: call the menu room
