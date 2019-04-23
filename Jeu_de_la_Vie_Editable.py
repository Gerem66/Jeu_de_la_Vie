#!/usr/bin/env python3
# coding: utf8

# Jeu de la vie (Jeu_de_la_Vie_Editable.py + Game_Of_Life.py)
# Temps : ~1h
# Par : Geremy

import Game_Of_Life as GOL
from Game_Of_Life import GetInt, GetFloat, GetString, Clear

Clear()

try:
    width = GetInt("Entrez la largeur du tableau (5-300) : ", 5, 300)
    height = GetInt("Entrez la longueur du tableau (5-100) : ", 5, 100)
    speed_game = GetFloat("Vitesse de développement (0.001-2) : ", 0.001, 2)
    rand_str = GetString("Générer le tableau aléatoirement (O/N) ? ", ["y", "o", "n"])
    rand = False if rand_str == "n" else True
except KeyboardInterrupt:
    print("Fin de la simulation : Interruption par l'utilisateur.")
    exit()

game = GOL.Game_of_Life(speed_game, width, height, rand)