# -----------------------------------------------------------------------------
# Created by Ulysses Carlos on 07/06/2020 at 02:41 PM
#
# Scene.py
# All classes related to each individual scene is stored here.
# -----------------------------------------------------------------------------

# Base Scene handles song that plays in each room, alongside a XML
# file that handles dialog,
from os import path
from sys import exit
from textwrap import dedent
from textwrap import fill
from pathlib import Path
from time import sleep
import xmltodict

# Handles the time to display each line.
line_pause_length = 4.25
prompt_character = "> "
text_path = Path.cwd()
# line_pause_length = 0


class BaseScene(object):
    def __init__(self, xml_file_path):
        # Now check if the file can be open at all:
        check_path = path.exists(xml_file_path)
        if not check_path:
            error_message = f"The file \"{xml_file_path}\" does not exist."
            raise OSError(error_message)
        else:
            self.xml_file_path = xml_file_path
            # Set the initial flag (For scenes) to the first scene:
            self.scene_flag = "initial"
            # Now open the xml file, store the scenes
            with open(self.xml_file_path, 'r') as fstream:
                self.xml_file = xmltodict.parse(fstream.read())
                self.scene_list = self.xml_file["room"]["scene-list"]
            # Now set a toggle for the base_scene
            self.is_base_scene = True

    def print_dialog(self, scene_string, line_speed):
        """
        Prints text at a specified text-speed. line_speed determines the time 
        it takes to print a single line.
        """
        list = scene_string.split("\n")
        for i in range(0, len(list)):
            print(fill(dedent(list[i]), 80))
            sleep(float(line_speed))

    def print_options(self, option_list):
        # Store all the options in a list
        options = list(option_list)
        for i in range(0, len(options)):
            print(f"{chr(ord('a') + i)}) {option_list[options[i]]['name']}")

    def check_input(self, option_list, string):
        options = len(list(option_list))

        end = str(chr(ord('a') + options))

        return ("a" <= string and string < end)

    def get_user_input(self, options_list):
        """
        Prints the available options and allows the user to choose.
        Returns the option key if the user inputs an valid option.

        """
        # self.print_options(options_list)
        user_input = input(prompt_character)
        # Clean input in case.
        if len(user_input) > 1:
            user_input = str(user_input[0])

        while not (self.check_input(options_list, user_input)):
            print("Hey, that's not an option that I can choose. "
                  + "Why not try one of the options in the list?"
                  )
            user_input = input(prompt_character)
            # Repeat
            if len(user_input) > 1:
                user_input = str(user_input[0])

        as_list = list(options_list)
        result = as_list[(ord(user_input) - ord('a'))]
        return result

    def enter_scene(self):
        if self.is_base_scene:
            print("ERROR: You have tried to enter a scene that is defined"
                  + " as a base scene. Make sure that the is_base_scene "
                  + "variable is set to False in your derived class.")
            exit(1)

        # Make a difference between (scene) and (scene with options)
        self.current_room_scene = self.scene_list[self.scene_flag]
        # Get the type of scene:
        self.current_room_scene_type = self.current_room_scene["@type"]

        if not (self.current_room_scene_type == "conversation" or
                self.current_room_scene_type == "menu" or
                self.current_room_scene_type == "action"):
            scene_name = list(self.scene_list)[0]
            print("ERROR: The scene "
                  + scene_name
                  + "in "
                  + self.xml_file_path
                  + " is not defined as a conversation, menu, or action."
                  + "Please fix that.")
            exit(1)

        # Now play music.
        if self.current_room_scene_type == "conversation":
            # Print any actors if defined in actors
            actor_check = self.current_room_scene["actors"]

            if actor_check["is-empty"] == 'false':
                # Print Ryouko:
                with open("./ascii/pychologist_bw.txt", "r") as fstream:
                    print(fstream.read())

            self.print_dialog(self.current_room_scene["opening"],
                              line_pause_length)
            # first, print the opening (if defined).
            self.print_dialog(self.current_room_scene["dialog"],
                              line_pause_length)
            # then increment the scene_flag and go to next room
            self.scene_flag = self.current_room_scene["next-scene"]
            # Then return next room
            return self.current_room_scene["next-room"]
        elif (self.current_room_scene_type == "action" or
              self.current_room_scene_type == "menu"):

            # Set the line speed depending on room type
            if self.current_room_scene_type == "action":
                self.print_dialog(self.current_room_scene["opening"],
                                  line_pause_length)
            else:
                self.print_dialog(self.current_room_scene["opening"],
                                  0)

            print("")
            # Now display options and allow user to take input.
            self.print_options(self.current_room_scene["option-list"])
            key = self.get_user_input(self.current_room_scene["option-list"])
            # Print a newline to seperate text and options

            option = self.current_room_scene["option-list"][key]

            while (option["type"] == "text"):
                # Print text:
                self.print_dialog(option["selection"], line_pause_length)
                # print(option["selection"])
                key = self.get_user_input(self.current_room_scene["option-list"])
                option = self.current_room_scene["option-list"][key]

            if option["type"] == "room-change":
                self.print_dialog(option["selection"], line_pause_length)
                # return option["next-scene-name"]
                self.scene_flag = option["next-scene"]
                return option["next-room"]
            elif option["type"] == "scene-change":
                # Set the flag to the scene-change and then call enter_scene
                # again.
                self.print_dialog(option["selection"], line_pause_length)
                # self.scene_flag = key
                self.scene_flag = self.current_room_scene["next-scene"]
                self.enter_scene()
            elif option["type"] == "quit":
                self.print_dialog(option["selection"], line_pause_length)
                exit(1)


class PyschRoomScene(BaseScene):
    def __init__(self):
        # file_name = "./text/Psychologist_Room.xml"
        file_name = text_path / "text" / "Psychologist_Room.xml"
        super(PyschRoomScene, self).__init__(file_name)
        self.is_base_scene = False


class ApartmentRoomScene(BaseScene):
    def __init__(self):
        # file_name = "./text/Apartment.xml"
        file_name = text_path / "text" / "Apartment.xml"
        super(ApartmentRoomScene, self).__init__(file_name)
        self.is_base_scene = False


class SaveRoomScene(BaseScene):
    def __init__(self):
        # file_name = "./text/Save_Point.xml"
        file_name = text_path / "text" / "Save_Point.xml"
        super(SaveRoomScene, self).__init__(file_name)
        self.is_base_scene = False


class HospitalRoomScene(BaseScene):
    def __init__(self):
        # file_name = "./text/Xenon_Hospital_Room.xml"
        file_name = text_path / "text" / "Xenon_Hospital_Room.xml"
        super(HospitalRoomScene, self).__init__(file_name)
        self.is_base_scene = False


class LeftCorridorScene(BaseScene):
    def __init__(self):
        # file_name = "./text/Xenon_Left_Corridor.xml"
        file_name = text_path / "text" / "Xenon_Left_Corridor.xml"
        super(LeftCorridorScene, self).__init__(file_name)
        self.is_base_scene = False


class RightCorridorScene(BaseScene):
    def __init__(self):
        # file_name = "./text/Xenon_Right_Corridor.xml"
        file_name = text_path / "text" / "Xenon_Right_Corridor.xml"
        super(RightCorridorScene, self).__init__(file_name)
        self.is_base_scene = False


class ObservatoryRoomScene(BaseScene):
    def __init__(self):
        # file_name = "./text/Xenon_Observatory_Room.xml"
        file_name = text_path / "text" / "Xenon_Observatory_Room.xml"
        super(ObservatoryRoomScene, self).__init__(file_name)
        self.is_base_scene = False


class CryrogenicRoomScene(BaseScene):
    def __init__(self):
        # file_name = "./text/Xenon_Cryogenic_Room.xml"
        file_name = text_path / "text" / "Xenon_Cryogenic_Room.xml"
        super(CryrogenicRoomScene, self).__init__(file_name)
        self.is_base_scene = False


class OpeningRoomScene(BaseScene):
    def __init__(self):
        # file_name = "./text/Opening.xml"
        file_name = text_path / "text" / "Opening.xml"
        super(OpeningRoomScene, self).__init__(file_name)
        self.is_base_scene = False


class EndRoomScene(BaseScene):
    def __init__(self):
        # file_name = "./text/End.xml"
        file_name = text_path / "text" / "End.xml"
        super(EndRoomScene, self).__init__(file_name)
        self.is_base_scene = False


class MainMenuScene(BaseScene):
    def __init__(self):
        # file_name = "./text/Main_Menu.xml"
        file_name = text_path / "text" / "Main_Menu.xml"
        super(MainMenuScene, self).__init__(file_name)
        self.is_base_scene = False
