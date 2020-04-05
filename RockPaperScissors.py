import random


player = input("Let's play Rock, Paper, Scissors.  Choose one of them.")
game = ['ROCK', 'PAPER', 'SCISSORS']
computer = random.choice(game)

def play_game (player):
    if player.upper() == 'ROCK':
        if computer == 'ROCK':
            return "tie"
        elif computer == 'SCISSORS':
            return "player wins"
        else:
            return "computer wins"
    if player.upper() == 'PAPER':
        if computer == 'PAPER':
            return "tie"
        elif computer == 'ROCK':
            return "player wins"
        else:
            return "computer wins"
    if player.upper() == 'SCISSORS':
        if computer == 'SCISSORS':
            return "tie"
        elif computer == 'PAPER':
            return "player wins"
        else:
            return "computer wins"


while True:
    if player.upper() not in game:
        player = input("Sorry, I didn't recognize that choice, try again")
    else:
        print(play_game(player))
        break