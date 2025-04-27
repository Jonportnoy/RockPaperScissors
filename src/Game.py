from random import randint

from src.Paper import Paper
from src.Rock import Rock

def play(player1, player2):
    if isinstance(player1, Rock) and isinstance(player2, Paper):
        return player2
def opponent_played():
    op_play = randint(0,2)
    return ['Rock', 'Paper', 'Scissors'][op_play]