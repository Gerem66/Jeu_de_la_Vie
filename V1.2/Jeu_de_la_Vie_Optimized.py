import os
import time
import random

Width, Heigth, fps = 80, 10, 0.1
Map = [[random.randint(0, 1) for _ in range(Heigth)] for _ in range(Width)]

def CheckAround(x, y):
    n = 0
    if x != 0 and y != 0 and x != Width - 1 and y != Heigth - 1:
        for D in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            if Map[x + D[0]][y + D[1]] == 1: n += 1
    return n

while True:
    # Show
    os.system("cls || clear")
    for y in range(Heigth):
        for x in range(Width):
            print("█" if Map[x][y] == 1 else " ", end='')
        print("")
    # Next Step
    _Map = [[0 for _ in range(Heigth)] for _ in range(Width)]
    for y in range(Heigth):
        for x in range(Width):
            if ((CheckAround(x, y) == 2 or CheckAround(x, y) == 3) and Map[x][y] == 1) or (Map[x][y] == 0 and CheckAround(x, y) == 3):
                _Map[x][y] = 1
    Map = _Map
    time.sleep(fps)
