class Score:
    def __init__(self):
        self.x_score = 0
        self.o_score = 0
        self.draw_score = 0

    def __str__(self):
        return (f'Final score:'
                f'\n"X" - {self.x_score}'
                f'\n"O" - {self.o_score}'
                f'\nFriendship - {self.draw_score}')
