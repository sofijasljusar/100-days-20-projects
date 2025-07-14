from board import Board
from game import Game
from player import Player
from score import Score

board = Board(3, 3)
player1 = Player("X")
player2 = Player("O")
score = Score()
game = Game(board, player1, player2, score)
game.start_game()
