#!/usr/bin/env python3
# coding: utf8

import os
import sys
import time
import random
import platform

try:
    if platform.system() == "Linux": import getch
    else: import msvcrt as getch
except ImportError:
    if platform.system() == "Linux":
        print("getch n'est pas installé...\nVeuillez l'installer")
        print("Install 'pip3' :\ncurl \"https://bootstrap.pypa.io/get-pip.py\" -o \"get-pip.py\"\npython3 get-pip.py --user")
        print("Install 'getch' with 'pip3' :\npip3 install py-getch")
    else:
        print("Vous devez installer la librairie 'msvcrt' pour continuer.")
    exit()

class Game_of_Life:

    """ DocString for the Game of Life
    
    Parameters :
    speed_game (int):           Duration of a frame
    width, height (int, int):   Size of the array
    random (bool):              True: randomize generation, False: manual generation
    abort (bool):               Quit instantly class (used to get initial variables (like clear_command))

    """

    def __init__(self, speed_game, width, height, random, abort = False):

        # Set global variables
        self.clear_command = "clear" if platform.system() == "Linux" else "cls"
        self.Width = width
        self.Height = height
        self.Random = random
        self.Speed_Game = speed_game

        # Abort used to clear function
        if abort: return

        # Generate Map
        self.Generate_Map()

        # Live
        Alive = True
        while Alive:
            try:
                Alive = self.NextStep()
                if not Alive:
                    print("Fin de la simulation : version stable atteinte.")
            except KeyboardInterrupt:
                print("Fin de la simulation : Interruption par l'utilisateur.")
                Alive = False


    # Génération du tableau (ahutomatiquement ou aléatoirement)
    def Generate_Map(self):
        if self.Random:
            # Random Map
            self.Map = [[random.randint(0, 1) for _ in range(self.Height)] for _ in range(self.Width)]
        else:
            # Empty Map then Edit Mode
            self.Map= [[0 for _ in range(self.Height)] for _ in range(self.Width)]
            
            # Edit Mode
            x, y, C = 0, 0, b''
            while C != b'\r':
                self.Show(True, x, y)
                C = getch.getch()
                if C == b'z' and y > 0:
                    y -= 1
                if C == b's' and y < self.Height - 1:
                    y += 1
                if C == b'q' and x > 0:
                    x -= 1
                if C == b'd' and x < self.Width - 1:
                    x += 1
                if C == b'e':
                    self.Map[x][y] = 0 if self.Map[x][y] == 1 else 1

    
    # Affichage du tableau
    def Show(self, EditMode = False, Edit_X = -1, Edit_Y = -1):
        # Clear
        os.system(self.clear_command)

        # Edit Mode
        if EditMode:
            print("Edition Mode [ z,q,s,d => Move | e => Add / Remove block | enter => Valid ]")

        # First Line
        print("╔", end='')
        for _ in range(self.Width):
            print("═", end='')
        print("╗")

        # Map
        for y in range(self.Height):
            print("║", end='')
            for x in range(self.Width):
                if EditMode and x == Edit_X and y == Edit_Y:
                    if self.Map[x][y] == 0:
                        print("X", end='')
                    else:
                        print("▒", end='')
                elif self.Map[x][y] == 1:
                    print("█", end='')
                else:
                    print(" ", end ='')
            print("║")

        # Last Line
        print("╚", end='')
        for _ in range(self.Width):
            print("═", end='')
        print("╝")

    # Nombre de cases en vie autour de la case (x, y)
    def CheckAround(self, x, y):
        n = 0
        if x == 0 or y == 0 or x >= self.Width - 1 or y >= self.Height - 1:
            return 0
        if self.Map[x - 1][y - 1] == 1: n += 1
        if self.Map[x - 1][y] == 1: n += 1
        if self.Map[x - 1][y + 1] == 1: n += 1
        if self.Map[x][y - 1] == 1: n += 1
        if self.Map[x][y + 1] == 1: n += 1
        if self.Map[x + 1][y - 1] == 1: n += 1
        if self.Map[x + 1][y] == 1: n += 1
        if self.Map[x + 1][y + 1] == 1: n += 1
        return n

    # Next Step
    def NextStep(self):
        _Map = [[0 for _ in range(self.Height)] for _ in range(self.Width)]
        for x in range(self.Width):
            for y in range(self.Height):
                if (self.CheckAround(x, y) == 2 or self.CheckAround(x, y) == 3) and self.Map[x][y] == 1:
                    _Map[x][y] = 1
                if self.Map[x][y] == 0 and self.CheckAround(x, y) == 3:
                    _Map[x][y] = 1
        if self.Map == _Map: return False
        self.Map = _Map
        self.Show()
        time.sleep(self.Speed_Game)
        return True

def Clear():
    os.system(Game_of_Life(0, 0, 0, False, True).clear_command)
    
    print("╔═══════════════════════════╗")
    print("║        Game of Life       ║")
    print("║             by            ║")
    print("║           Gerem           ║")
    print("╚═══════════════════════════╝\n\n")


def GetInt(Prompt, min, max, default):
    try:
        var = input(Prompt + " [" + str(min) + "-" + str(max) + "] (" + str(default) + ") : ")
        if var == "": var = default
        var = int(var)
        if var < min or var > max:
            var = int(".")
        return var
    except ValueError:
        print("Veuillez entrer une valeur correcte !")
        GetInt(Prompt, min, max, default)


def GetFloat(Prompt, min, max, default):
    try:
        var = input(Prompt + " [" + str(min) + "-" + str(max) + "] (" + str(default) + ") : ")
        if var == "": var = default
        var = float(var)
        if var < min or var > max:
            var = float(".")
        return var
    except ValueError:
        print("Veuillez entrer une valeur correcte !")
        GetFloat(Prompt, min, max, default)


def GetString(Prompt, vals, default):
    try:
        # All lower
        for v in range(len(vals)):
            vals[v] = vals[v].lower()
        var = input(Prompt).lower()
        if var == "": var = default
        for v in vals:
            if var == v:
                return var
        var = float("")
    except ValueError:
        print("Veuillez entrer une valeur correcte !")
        GetString(Prompt, vals, default)