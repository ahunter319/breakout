from turtle import Screen
from paddle import Paddle
from brickmanager import BrickManager
from ball import Ball
from scoreboard import Scoreboard
import sys
import os


def resource_path(relative_path):
    """ Get the absolute path to the resource.
    (borrowed from Stackoverflow: https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile) """
    try:
        # Pyinstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Constants
WIDTH = 900
HEIGHT = 700
ANGLES = {
    0: 150,
    1: 135,
    2: 120,
    3: 90,
    4: 60,
    5: 45,
    6: 30
}

speed_scales = {
    "green": 1.2,
    "yellow": 1.5,
    "orange": 2.0,
    "red": 2.5
}

# Initializing screen object
screen = Screen()
screen.title("BREAKOUT")
root = Screen()._root
icon = resource_path('favicon.ico')
root.iconbitmap(icon)
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

# Initializing paddle, brickmanager, ball, and scoreboard objects
paddle = Paddle()
brickmanager = BrickManager()
ball = Ball()
scoreboard = Scoreboard()

# Binding keys
screen.listen()
screen.onkeypress(paddle.left, "a")
screen.onkeypress(paddle.right, "d")


# Game loop
game_is_on = True
while game_is_on:

    screen.update()

    ball.move()

    # Detect collision between ball and paddle
    for n in range(len(paddle.parts)-1):
        if paddle.parts[n].distance(ball) < 30:
            if ball.heading() > 270:
                angle = ANGLES[6-n]
                ball.bounce(angle)
            else:
                angle = ANGLES[n]
                ball.bounce(angle)

    # Detect collision between ball and bricks
    for brick in brickmanager.bricks:
        for chunk in brick:
            if chunk.distance(ball) < 20:
                color = chunk.color()[0]
                ball.speed = speed_scales[color]
                brickmanager.remove_brick(brick)
                scoreboard.add_point(color)
                angle = -(ball.heading())
                ball.bounce(angle)

    # Detect collision between ball and wall
    angle = ball.heading()
    if ball.xcor() > (WIDTH/2):
        ball.bounce(180-angle)
    elif ball.xcor() < -(WIDTH/2):
        ball.bounce(180-angle)
    elif ball.ycor() < -(HEIGHT/2):
        scoreboard.lose_life()
        ball.reset_ball()
    elif ball.ycor() > (HEIGHT/2):
        ball.bounce(-angle)

    # Kill game if out of lives or bricks
    if scoreboard.lives < 0:
        scoreboard.game_over("GAME OVER")
        ball.clear()
        game_is_on = False
    elif len(brickmanager.bricks) <= 0:
        scoreboard.game_over("YOU WIN")
        ball.clear()
        game_is_on = False

screen.exitonclick()

