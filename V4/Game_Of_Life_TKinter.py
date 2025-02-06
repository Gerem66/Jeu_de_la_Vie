#!/usr/bin/env python3
# coding: utf8

import os
import sys
import random
import platform
from tkinter import *

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
    length (int):               Length of cells
    random (bool):              True: randomize generation, False: manual generation
    abort (bool):               Quit instantly class (used to get initial variables (like clear_command))

    """

    def __init__(self, speed_game, width, height, cell_len, Random, abort = False):

        # Set global variables
        self.clear_command = "clear" if platform.system() == "Linux" else "cls"
        self.Width = width
        self.Height = height
        self.Random = Random
        self.Speed_Game = int(speed_game * 1000)
        self.length = cell_len
        self.Run = True
        self.DarkTheme = False
        
        self.Theme()

        # Abort used to clear function
        if abort: return

        # Live
        # Alive = True
        self.graph = Tk()
        self.Title()
        self.graph.bind("<Button-1>", self.on_click)
        self.graph.bind("<Return>", self.on_enter)
        self.graph.bind("r", self.on_reset)
        self.graph.bind("R", self.on_reset)
        self.graph.bind("a", self.on_random)
        self.graph.bind("A", self.on_random)
        self.graph.bind("+", self.on_add)
        self.graph.bind("-", self.on_sub)
        self.graph.bind("t", self.on_theme)
        self.graph.bind("T", self.on_theme)
        self.graph.resizable(False, False)

        self.dessin = Canvas(self.graph, width=self.Width * self.length, height=self.Height * self.length, bg=self.color_bg, bd=8)
        self.dessin.pack()

        # Generate Map
        self.Generate_Map()

        # Init loop
        self.graph.after(0, self.NextStep)
        self.graph.mainloop()
        
        # graph.destroy()

    def Title(self):
        state = "Play" if self.Run else "Pause"
        self.graph.title("Jeu de la vie [ Vitesse : " + str(self.Speed_Game) + "ms ] [ " + state + " ]")

    def on_theme(self, event):
        self.Theme()
        self.Show()

    def Theme(self):
        if not self.DarkTheme:
            self.color_bg = "white"
            self.color_cell = "black"
            self.color_grid = "black"
        # Thème sombre
        else:
            self.color_bg = "black"
            self.color_cell = "white"
            self.color_grid = "black"
        self.DarkTheme = not self.DarkTheme

    def on_add(self, event):
        self.Speed_Game += 10
        if self.Speed_Game > 5000:
            self.Speed_Game = 5000
        self.Title()

    def on_sub(self, event):
        self.Speed_Game -= 10
        if self.Speed_Game < 10:
            self.Speed_Game = 10
        self.Title()

    def on_click(self, event):
        # print("Click : " + str(event.x) + ", " + str(event.y))
        if event.x < self.length or event.y < self.length or event.x > self.Width * self.length or event.y > self.Height * self.length:
            return
        self.Map[int(event.x / self.length)][int(event.y / self.length)] = abs(self.Map[int(event.x / self.length)][int(event.y / self.length)] - 1)
        self.Show()

    def on_enter(self, event):
        self.Run = not self.Run
        self.Title()
        if self.Run: self.NextStep()

    def on_reset(self, event):
        self.Map = [[0 for _ in range(self.Height)] for _ in range(self.Width)]
        self.Run = False
        self.Title()
        self.Show()
    
    def on_random(self, event):
        self.Map = [[random.randint(0, 1) for _ in range(self.Height)] for _ in range(self.Width)]
        self.Run = False
        self.Title()
        self.Show()

    # Génération du tableau (ahutomatiquement ou aléatoirement)
    def Generate_Map(self):
        if self.Random:
            # Random Map
            self.Map = [[random.randint(0, 1) for _ in range(self.Height)] for _ in range(self.Width)]
        else:
            # Empty Map then Edit Mode
            self.Map= [[0 for _ in range(self.Height)] for _ in range(self.Width)]
            
            # Edit Mode
            self.Run = False
            self.Title()
            self.Show()

    # Affichage du tableau
    def Show(self, EditMode = False, Edit_X = -1, Edit_Y = -1):
        ## Graphical Mode
        # Clear
        self.dessin.pack_forget()
        self.dessin = Canvas(self.graph, width=self.Width * self.length, height=self.Height * self.length, bg=self.color_bg, bd=8)
        
        # Show Grid
        for i in range(self.Width + 1): # Vertical
            self.dessin.create_line(self.length * i, self.length, self.length * i, self.Height * self.length, fill=self.color_grid)
        for i in range(self.Height + 1): # Horizontal
            self.dessin.create_line(self.length, self.length * i, self.Width * self.length, self.length * i, fill=self.color_grid)

        # Show cells
        for y in range(self.Height):
            for x in range(self.Width):
                if x == 0 or y == 0:
                    continue
                if self.Map[x][y] == 1:
                    self.dessin.create_rectangle(self.length * x, self.length * y, self.length * (x+1), self.length * (y+1), fill=self.color_cell)
        
        # Draw
        self.dessin.pack()
        
        #################

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
        # Stop loop
        if not self.Run: return
        _Map = [[0 for _ in range(self.Height)] for _ in range(self.Width)]
        for x in range(self.Width):
            for y in range(self.Height):
                if (self.CheckAround(x, y) == 2 or self.CheckAround(x, y) == 3) and self.Map[x][y] == 1:
                    _Map[x][y] = 1
                if self.Map[x][y] == 0 and self.CheckAround(x, y) == 3:
                    _Map[x][y] = 1
        self.Map = _Map
        self.Show()
        # Loop
        self.graph.after(self.Speed_Game, self.NextStep)

def Clear():
    os.system(Game_of_Life(0, 0, 0, 0, False, True).clear_command)
    
    print("╔═════════════════════════════════╗")
    print("║  Game of Life (Graphical Mode)  ║")
    print("║                by               ║")
    print("║              Gerem              ║")
    print("╚═════════════════════════════════╝\n\n")
    print("Commandes :\n- Left click\tAdd / Remove cell\n- Enter\t\tPlay / Pause\n- -/+\t\tIncreases or Reduces time\n- A\t\tRandomize grid\n- R\t\tReset grid\n- T\t\tSwitch Light / Dark Theme\n\n")


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
