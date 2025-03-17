# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 11:23:24 2025

@author: 90531
"""

import random

def player(prev_play, opponent_history = []):
    # If it's the first game, make a random move
    if prev_play == "":
        return random.choice(["R", "P", "S"])

    # Add the opponent's previous move to the history
    opponent_history.append(prev_play)

    # Basic strategy: check the most frequent move of the opponent
    # If the opponent played Rock, counter with Paper
    if opponent_history.count('R') > opponent_history.count('P') and opponent_history.count('R') > opponent_history.count('S'):
        return 'P'  # Paper beats Rock
    # If the opponent played Paper, counter with Scissors
    elif opponent_history.count('P') > opponent_history.count('R') and opponent_history.count('P') > opponent_history.count('S'):
        return 'S'  # Scissors beats Paper
    # If the opponent played Scissors, counter with Rock
    elif opponent_history.count('S') > opponent_history.count('R') and opponent_history.count('S') > opponent_history.count('P'):
        return 'R'  # Rock beats Scissors
    else:
        # If all counts are equal or no clear pattern, choose randomly
        return random.choice(["R", "P", "S"])
