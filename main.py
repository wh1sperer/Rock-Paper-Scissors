# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 11:24:23 2025

@author: 90531
"""

from RPS_game import play
from RPS import player, quincy  # Assuming quincy is another bot

# Run a match of 1000 games between 'player' and 'quincy'
play(player, quincy, 1000, verbose=True)
