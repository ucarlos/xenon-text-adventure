
# -----------------------------------------------------------------------------
# Created by Ulysses Carlos on 07/07/2020 at 10:10 PM
#
# Engine.py
# Contains the classes needed to run the text portion of the game.
# -----------------------------------------------------------------------------

import Scene
from os import system

class Engine(object):
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

    def __init__(self):
        # Set the first and last rooms for the game
        self.first_room = self.room_list["main-menu"]
        self.last_room = self.room_list["end"]

    def start_game(self):
        # First, set the current room to first room:
        current_room = self.first_room

        while current_room != self.last_room:
            next_room_name = current_room.enter_scene()
            # Clear the screen.
            system("clear")
            # Find the room with that name and continue.
            current_room = self.room_list[next_room_name]

        # End the game on end-room:
        # TODO: call the menu room
