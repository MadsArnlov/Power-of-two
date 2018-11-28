# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:08:51 2018

@author: bergl
"""

import numpy as np

import PowerOfTwo as POT
user="Superuser The one to rule them all"

difficulty=input("what difficulty would you like to fluekneppe? easy/medium/hard =").upper()
if difficulty == "EASY":
        POT.easy()
    elif difficulty == "MEDIUM":
        POT.medium()
    elif difficulty == "HARD":
        POT.hard()

