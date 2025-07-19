from turtle import Turtle
from settings import OBJECT_COLOR, TOP_BORDER, BOTTOM_BORDER, RIGHT_BORDER, LEFT_BORDER
from random import randint

START_X = 0
START_Y = BOTTOM_BORDER + 60


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.speed(1)
        self.color(OBJECT_COLOR)
        self.set_random_direction()
        self.move_distance = 10
        self.restart()

    def set_random_direction(self):
        angle = randint(45, 135)
        self.setheading(angle)
        self.tiltangle(-angle)

    def move(self):
        self.forward(self.move_distance)

    def hit_top_wall(self):
        y = self.ycor()
        if y > TOP_BORDER-20:
            return True

    def hit_side_wall(self):
        x = self.xcor()
        if x > RIGHT_BORDER-20 or x < LEFT_BORDER+20:
            return True

    def bounce_vertically(self):
        old_angle = self.heading()
        bounce_angle = (old_angle * -1) % 360
        distance_traveled = bounce_angle - old_angle
        self.setheading(bounce_angle)
        self.tilt(-distance_traveled)

    def bounce_horizontally(self):
        old_angle = self.heading()
        bounce_angle = (180 - old_angle)
        distance_traveled = bounce_angle - old_angle
        self.setheading(bounce_angle)
        self.tilt(-distance_traveled)

    def restart(self):
        self.goto(START_X, START_Y)
        self.set_random_direction()
        self.move_distance = 10
