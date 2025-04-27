from src.Paper import Paper
from src.Rock import Rock


def play(player1, player2):
    if isinstance(player1, Rock) and isinstance(player2, Paper):
        return player2
def opponent_played():
    return "none"