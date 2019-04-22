import os
import time
import random

length = 50
Map = [[random.randint(0, 1) for _ in range(length)] for _ in range(length)] # Random Map

def Show():
    os.system("cls")
    for x in range(length):
        for y in range(length):
            if Map[x][y] == 1:
                print("█", end='')
            else:
                print(" ", end ='')
        print("")
    
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

while True:
    _Map = [[0 for _ in range(length)] for _ in range(length)]
    for x in range(length):
        for y in range(length):
            if (CheckAround(x, y) == 2 or CheckAround(x, y) == 3) and Map[x][y] == 1:
                _Map[x][y] = 1
            if Map[x][y] == 0 and CheckAround(x, y) == 3:
                _Map[x][y] = 1
    Map = _Map
    Show()
    time.sleep(.05)