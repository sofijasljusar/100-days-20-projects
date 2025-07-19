from turtle import Turtle
from settings import OBJECT_COLOR


class Block(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=0.5, stretch_len=2)
        self.penup()
        self.color(OBJECT_COLOR)
        self.goto(x, y)

    def destroy(self):
        self.goto(1000, 1000)
