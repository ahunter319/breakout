from turtle import Turtle
import random

MOVE_DISTANCE = 4


class Ball(Turtle):
    """
    Ball class inherits from the Turtle class and is used to create the game's ball and handle its movement and
    collisions.

    Methods:
        __init__(self)
        move(self)
        bounce(self)
        reset_ball(self)
    """

    def __init__(self):
        super().__init__()
        """
        Ball class constructor to initialize the object.
        """
        # Initial attributes/turtle methods
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto((0, 10))
        self.setheading(random.randrange(210, 330))
        self.speed = 1.0

    def move(self):
        """
        Moves ball at variable speed.
        """

        self.forward(MOVE_DISTANCE * self.speed)

    def bounce(self, direction):
        """
        Changes ball's direction and calls move method.
        :param direction: Angle, given as integer.
        """

        self.setheading(direction)
        self.move()

    def reset_ball(self):
        """
        Resets ball's speed, returns to origin, and chooses random direction to move.
        """

        self.speed = 1.0
        self.setheading(random.randrange(210, 330))
        self.goto((0, 10))

