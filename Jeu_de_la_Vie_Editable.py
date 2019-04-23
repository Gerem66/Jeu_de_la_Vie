#!/usr/bin/env python3
# coding: utf8

import Game_Of_Life as GOL
from Game_Of_Life import GetInt, GetFloat, GetString, Clear

Clear()
width = GetInt("Entrez la largeur du tableau (5-100) : ", 5, 100)
height = GetInt("Entrez la longueur du tableau (5-100) : ", 5, 100)
speed_game = GetFloat("Vitesse de développement (0.001-2) : ", 0.001, 2)
rand_str = GetString("Générer le tableau aléatoirement (O/N) ? ", ["y", "o", "n"])
rand = False if rand_str == "n" else True

game = GOL.Game_of_Life(speed_game, width, height, rand)