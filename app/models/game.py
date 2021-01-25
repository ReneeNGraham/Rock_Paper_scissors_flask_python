class Game():

    def __init___(self, player1, player2, computer):
        self.player1 = player1
        self.player2 = player2
        self.computer = computer

choice = ["rock", "paper", "scissors"]
    
player1 = input("Player1 name:  "), input("Choose Rock, Paper, or Scissors:  ").lower()
player2 = input("Player2 name:   "), input("Choose Rock, Paper, or Scissors: ").lower()

players = [player1, player2]

def play_game(self, player1, player2):

    if player1.choice == player2.choice:
        return "It is a draw, try again!"
    elif (player1.choice == "Paper" and player2.choice == "Rock") or (player1.choice == "Scissors" and player2.choice == "Paper") or (player1.choice == "Rock" and player2.choice == "Scissors"):
        return player1 + "wins this round!"
    elif (player1.choice == "Scissors" and player2.choice == "Rock") or (player1.choice == "Rock" and player2.choice == "Paper") or (player1.choice == "Paper" and player2.choice == "Scissors"):
        return player2 + "wins this round!"
    else:
        return None

        

        







        
