class Player:
    def __init__(self, mark):
        self.mark = mark

    def get_move(self):
        """Returns a tuple of 2 integers"""
        while True:
            try:
                row = int(input("Select row (0-2): "))
                col = int(input("Select column (0-2): "))
                return row, col
            except ValueError:
                print("Please, enter a valid number.")

    def __str__(self):
        return self.mark
