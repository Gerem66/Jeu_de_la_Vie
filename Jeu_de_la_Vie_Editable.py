#!/usr/bin/env python3

import os
import sys
import time
import random

# Affichage du tableau
def Show(edit = False, edit_x = -1, edit_y = -1):
    # Clear
    os.system(clear_command)

    # Edit Mode
    if edit:
        print("Edition Mode [ z,q,s,d + enter => Move | E + enter => Add / Remove block | end + enter => Valid ]")

    # First Line
    print("╔", end='')
    for _ in range(length):
        print("═", end='')
    print("╗")

    # Map
    for x in range(length):
        print("║", end='')
        for y in range(length):
            if edit and x == edit_x and y == edit_y:
                print("X", end='')
            elif Map[x][y] == 1:
                print("█", end='')
            else:
                print(" ", end ='')
        print("║")

    # Last Line
    print("╚", end='')
    for _ in range(length):
        print("═", end='')
    print("╝")

# Nombre de cases en vie autour de la case (x, y)
def CheckAround(x, y):
    n = 0
    if x == 0 or y == 0 or y == length - 1 or x == length - 1:
        return 0
    if Map[x - 1][y - 1] == 1: n += 1
    if Map[x - 1][y] == 1: n += 1
    if Map[x - 1][y + 1] == 1: n += 1
    if Map[x][y - 1] == 1: n += 1
    if Map[x][y + 1] == 1: n += 1
    if Map[x + 1][y - 1] == 1: n += 1
    if Map[x + 1][y] == 1: n += 1
    if Map[x + 1][y + 1] == 1: n += 1
    return n

# Next Step
def NextStep():
    global Map
    _Map = [[0 for _ in range(length)] for _ in range(length)]
    for x in range(length):
        for y in range(length):
            if (CheckAround(x, y) == 2 or CheckAround(x, y) == 3) and Map[x][y] == 1:
                _Map[x][y] = 1
            if Map[x][y] == 0 and CheckAround(x, y) == 3:
                _Map[x][y] = 1
    Map = _Map
    Show()
    time.sleep(speed_game)

# Génération du tableau par l'utiliateur ou aléatoirement
clear_command = "cls"
os.system(clear_command)
length = -1
while length < 5 or length > 1000:
    length = int(input("Entrez la longueur du tableau (5-1000) : "))
speed_game = float(input("Vitesse de développement (1-0.001) : "))
rand = input("Générer le tableau aléatoirement (O/N) ? ")
if rand.lower() == "o" or rand.lower() == "y":
    Map = [[random.randint(0, 1) for _ in range(length)] for _ in range(length)]
elif rand.lower() == "n":
    # Edit Mode
    # Create Empty Map
    Map = [[0 for _ in range(length)] for _ in range(length)]
    # Add Creator
    x, y, I = 0, 0, -1
    while I != "end":
        Show(True, x, y)
        I = input("// ")
        I = I.lower()
        if I == "q":
            y -= 1
        if I == "d":
            y += 1
        if I == "z":
            x -= 1
        if I == "s":
            x += 1
        if I == "e":
            Map[x][y] = 0 if Map[x][y] == 1 else 1

# Main
while True:
    NextStep()