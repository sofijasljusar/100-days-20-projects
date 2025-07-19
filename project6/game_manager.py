import turtle as t
from settings import OBJECT_COLOR, BOTTOM_BORDER, TOP_BORDER, SMALL_FONT, BIG_FONT
import time

LIVES = 3


class LivesCount(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(OBJECT_COLOR)
        self.goto(210, TOP_BORDER-40)
        self.score = LIVES
        self.display_score()

    def display_score(self):
        self.write(arg=f"Lives: {self.score}", align="center", font=SMALL_FONT)

    def remove_life(self):
        self.clear()
        self.score -= 1
        self.display_score()

    def finish(self):
        return self.score == 0


class Text(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(OBJECT_COLOR)

    def write_welcome(self):
        self.write(arg="WELCOME TO THE BREAKOUT GAME!!!", align="center", font=BIG_FONT)
        t.update()
        time.sleep(1)
        self.clear()
        t.update()

    def game_lost(self):
        self.write(arg="YOU LOST!", align="center", font=BIG_FONT)
        t.update()
        time.sleep(1)
        self.clear()
        t.update()

    def game_won(self):
        self.write(arg="YOU WON!", align="center", font=BIG_FONT)
        t.update()
        time.sleep(1)
        self.clear()
        t.update()
