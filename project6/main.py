import turtle as t
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, BOTTOM_BORDER
from pad import Pad
from ball import Ball
import time
from game_manager import LivesCount, Text
from block import Block

screen = t.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title('BREAKOUT')
screen.bgcolor(BACKGROUND_COLOR)

t.listen()
t.tracer(0)

text = Text()
text.write_welcome()

pad = Pad()
ball = Ball()
lives_count = LivesCount()
blocks = []
for y in range(0, 76, 15):
    for x in range(-270, 271, 45):
        blocks.append(Block(x, y))
t.update()

t.onkey(pad.move_right, 'Right')
t.onkey(pad.move_left, 'Left')

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    t.update()
    ball.move()
    if ball.hit_side_wall():
        ball.bounce_horizontally()
    elif ball.hit_top_wall():
        ball.bounce_vertically()

    for block in blocks:
        if ball.distance(block) < 20:
            block.destroy()
            blocks.remove(block)
            ball.bounce_vertically()

    if ball.ycor() < BOTTOM_BORDER+40:
        if ball.distance(pad) < 40:
            ball.bounce_vertically()
            ball.move()
        else:
            lives_count.remove_life()
            ball.restart()

    if lives_count.finish():
        game_is_on = False
        text.game_lost()

    elif len(blocks) == 0:
        game_is_on = False
        text.game_won()


screen.exitonclick()
