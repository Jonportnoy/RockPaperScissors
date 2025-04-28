from random import randint


def play(player1: str, player2: str) -> str:
    a = "You Win"
    if player1 == "Rock" and player2 == "Paper":
        return a
    elif player1 == "Paper" and player2 == "Rock":
        return a
    elif player1 == "Scissors" and player2 == "Rock":
        return a
    else:
        return "Opponent Wins"
def opponent_played():
    op_play = randint(0,2)
    return ['Rock', 'Paper', 'Scissors'][op_play]