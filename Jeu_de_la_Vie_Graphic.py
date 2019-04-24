#!/usr/bin/env python3
# coding: utf8

# Jeu de la vie (Jeu_de_la_Vie_Graphic.py + Game_Of_Life_TKinter.py)

import Game_Of_Life_TKinter as GOL
from Game_Of_Life_TKinter import GetInt, GetFloat, GetString, Clear

# Automatic fill
'''width, height, length, speed_game, rand = 40, 40, 16, 0.1, False
game = GOL.Game_of_Life(speed_game, width, height, rand)
exit()'''

Clear()

try:
    width = GetInt("Entrez la largeur du tableau", 5, 500, 40)
    height = GetInt("Entrez la longueur du tableau", 5, 500, 40)
    cell_len = GetInt("Entrez la taille d'une cellule", 1, 48, 16)
    speed_game = GetFloat("Vitesse de développement", 0.001, 5, 0.1)
    rand_str = GetString("Générer le tableau aléatoirement [o/n] (o) ? ", ["y", "o", "n"], "o")
    rand = False if rand_str == "n" else True
except KeyboardInterrupt:
    print("Fin de la simulation : Interruption par l'utilisateur.")
    exit()

game = GOL.Game_of_Life(speed_game, width, height, cell_len, rand)