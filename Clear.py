import platform
from os import system
import os

def clear_screen():
    """
    Incomplete program to clear the screen.
    This program works for windows, linux, and macos, but any other os plaform may produce
    invalid results.
    """
    if platform.system() == "windows":
        system("cls")
    # Handle all posix options:
    elif os.name == "posix":
        system("clear")
    else:
        raise RuntimeError("Cannot clear screen on this OS.")
