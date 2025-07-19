from turtle import Turtle
from settings import OBJECT_COLOR, RIGHT_BORDER, LEFT_BORDER, BOTTOM_BORDER
RIGHT = 0
LEFT = 180
MOVE_DISTANCE = 30

START_X = 0
START_Y = BOTTOM_BORDER + 40


class Pad(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.setheading(RIGHT)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(OBJECT_COLOR)
        self.goto(START_X, START_Y)

    def move_right(self):
        if self.xcor() < RIGHT_BORDER-55:
            self.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.xcor() > LEFT_BORDER+40:
            self.back(MOVE_DISTANCE)
