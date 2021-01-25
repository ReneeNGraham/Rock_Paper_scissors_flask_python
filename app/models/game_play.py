from app.models.game import *
from app.models.player import *

choice = ["rock", "paper", "scissors"]
    
player1 = Player ("player 1", choice[])
player2 = Player ("player 2", choice[]) 
player_action = input("Enter a choice (rock, paper, scissors): ")

def play_game(self, player1, player2):
    if player1.choice == player2.choice:
        return "It is a draw, try again!"
    elif (player1.choice == "Paper" and player2.choice == "Rock") or (player1.choice == "Scissors" and player2.choice == "Paper") or (player1.choice == "Rock" and player2.choice == "Scissors"):
        return player1 + "wins this round!"
    elif (player1.choice == "Scissors" and player2.choice == "Rock") or (player1.choice == "Rock" and player2.choice == "Paper") or (player1.choice == "Paper" and player2.choice == "Scissors"):
        return player2 + "wins this round!"
    else:
        return None