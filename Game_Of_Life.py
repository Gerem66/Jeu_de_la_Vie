#!/usr/bin/env python3
# coding: utf8

import os
import time
import random

class Game_of_Life:

    """ DocString for the Game of Life """

    def __init__(self, speed_game, width, height, random, abort = False):

        # Set global variables
        self.clear_command = "cls" # "clear" for linux
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
            Alive = self.NextStep()


    # Génération du tableau (ahutomatiquement ou aléatoirement)
    def Generate_Map(self):
        if self.Random:
            # Random Map
            self.Map = [[random.randint(0, 1) for _ in range(self.Height)] for _ in range(self.Width)]
        else:
            # Empty Map then Edit Mode
            self.Map= [[0 for _ in range(self.Height)] for _ in range(self.Width)]
            
            # Edit Mode
            x, y, I = 0, 0, -1
            while I != "end":
                self.Show(True, x, y)
                I = input("// ")
                I = I.lower()
                for C in I:
                    if C == "z" and y > 0:
                        y -= 1
                    if C == "s" and y < self.Height - 1:
                        y += 1
                    if C == "q" and x > 0:
                        x -= 1
                    if C == "d" and x < self.Width - 1:
                        x += 1
                    if C == "e":
                        self.Map[x][y] = 0 if self.Map[x][y] == 1 else 1

    
    # Affichage du tableau
    def Show(self, EditMode = False, Edit_X = -1, Edit_Y = -1):
        # Clear
        os.system(self.clear_command)

        # Edit Mode
        if EditMode:
            print("Edition Mode [ z,q,s,d + enter => Move | E + enter => Add / Remove block | end + enter => Valid ]")

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
                    print("X", end='')
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
    print("=============================")
    print("|        Game of Life       |")
    print("|             by            |")
    print("|           Gerem           |")
    print("=============================\n\n")

def GetInt(Prompt, min = 0, max = 100):
    try:
        var = int(input(Prompt))
        if var < min or var > max:
            var = int(".")
        return var
    except ValueError:
        print("Veuillez entrer une valeur correcte !")
        GetInt(Prompt)

def GetFloat(Prompt, min = 0.001, max = 2):
    try:
        var = float(input(Prompt))
        if var < min or var > max:
            var = float(".")
        return var
    except ValueError:
        print("Veuillez entrer une valeur correcte !")
        GetFloat(Prompt)

def GetString(Prompt, vals):
    try:
        # All lower
        for v in range(len(vals)):
            vals[v] = vals[v].lower()
        var = input(Prompt).lower()
        for v in vals:
            if var == v:
                return var
        var = float("")
    except ValueError:
        print("Veuillez entrer une valeur correcte !")
        GetString(Prompt, vals)