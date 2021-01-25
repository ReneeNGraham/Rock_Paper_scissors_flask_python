from app.models.player import Player

choice = ["rock", "paper", "scissors"]
    
player1 = Player (input("Player1 name:  "), (input("Choose Rock, Paper, or Scissors:  ").lower()))
player2 = Player (input("Player2 name:   "), (input("Choose Rock, Paper, or Scissors: ").lower()))

players = [player1, player2]
  
