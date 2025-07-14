class Board:
    def __init__(self, rows, columns):
        self.height = rows
        self.width = columns
        self.state = None
        self.total_positions = self.height * self.width

    def move_is_valid(self, move):
        """Returns true if the passed tuple (row, col)
        fits into the board size
        and this position is not taken yet"""
        row = move[0]
        col = move[1]
        if row < 0 or row > len(self.state) - 1 or col < 0 or col > len(self.state[0]) - 1:
            print("Please, enter a number between 0 and 2.")
            return False
        elif self.state[row][col] != "-":
            print("This position is already taken.")
            return False
        return True

    def __str__(self):
        return "\n".join(" ".join(row) for row in self.state)

    def place_mark(self, mark, position):
        row = position[0]
        col = position[1]
        self.state[row][col] = mark

    def is_winner(self):
        """Returns winner mark or None"""
        # check rows
        for row in range(self.height):
            if self.state[row][0] == self.state[row][1] == self.state[row][2] != "-":
                return self.state[row][0]
        # check columns
        for col in range(self.width):
            if self.state[0][col] == self.state[1][col] == self.state[2][col] != "-":
                return self.state[0][col]
        # check diagonals
        if (self.state[0][0] == self.state[1][1] == self.state[2][2] != "-" or
                self.state[0][2] == self.state[1][1] == self.state[2][0] != "-"):
            return self.state[1][1]

    def reset_state(self):
        """Sets board to empty state"""
        self.state = [['-' for _ in range(self.width)] for _ in range(self.height)]
