from app import app
from flask import render_template, request
from app.models.player import *
from app.models.game import *
from random import randint

 
@app.route('/')
def index():
    return "Welcome to Rock Paper Scissors"

@app.route('/<player1_choice>/<player2_choice>')
def play(player1_choice, player2_choice):
    player1 = Player ("player 1", player1_choice)
    player2 = Player ("player 2", player2_choice)
    game = Game()

    return render_template('index html', player1=player1, player2=player2)

