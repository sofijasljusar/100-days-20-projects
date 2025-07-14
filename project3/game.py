import random


class Game:
    def __init__(self, board, player1, player2, score):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = None
        self.game_over = False
        self.score = score

    def set_first_player_randomly(self):
        self.current_player = random.choice([self.player1, self.player2])

    def play_one_round(self):
        moves_made = 0
        winner = self.board.is_winner()
        while moves_made < self.board.total_positions and not winner:
            print(f"{self.current_player}'s turn")
            move = self.current_player.get_move()
            while not self.board.move_is_valid(move):
                move = self.current_player.get_move()
            self.board.place_mark(self.current_player.mark, move)
            moves_made += 1
            print(self.board)
            winner = self.board.is_winner()
            if not winner:
                self.current_player = self.player2 if self.current_player == self.player1 else self.player1

        if winner:
            print(f"Player {winner} won!")
            if winner == "X":
                self.score.x_score += 1
            else:
                self.score.o_score += 1
        else:
            print("Friendship won. It's a draw.")
            self.score.draw_score += 1

    @staticmethod
    def play_again():
        return input("Do you want to play again (yes or no)? ")

    def start_game(self):
        while not self.game_over:
            self.board.reset_state()
            print(self.board)
            self.set_first_player_randomly()
            self.play_one_round()
            if self.play_again() != "yes":
                self.game_over = True
                print(self.score)
