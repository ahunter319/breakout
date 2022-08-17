from turtle import Turtle

WIDTH = 900
HEIGHT = 700
EDGE = WIDTH / 2
BOTTOM = -(HEIGHT / 2) + 40

POSITIONS = [(-60, BOTTOM), (-40, BOTTOM), (-20, BOTTOM), (0, BOTTOM), (20, BOTTOM), (40, BOTTOM), (60, BOTTOM)]
MOVE_DISTANCE = 40


class Paddle:
    """
    Paddle class is used to create and control the user's paddle.

    Methods:
        __init__(self)
        create_self(self)
        left(self)
        right(self)
    """

    def __init__(self):
        """
        Paddle class constructor to initialize the object.
        """

        self.parts = []
        self.length = len(POSITIONS) * 20
        self.create_self()

    def create_self(self):
        """
        Creates and places turtles in a row equal to the length of POSITIONS.
        """

        for position in POSITIONS:
            new_part = Turtle(shape="square")
            new_part.speed("fastest")
            new_part.color("white")
            new_part.setheading(0)
            new_part.penup()
            new_part.goto(position)
            self.parts.append(new_part)

    def left(self):
        """
        Moves the paddle left until it reaches the left wall.
        """
        if self.parts[0].xcor() > -EDGE:
            for part in self.parts:
                part.forward(-MOVE_DISTANCE)

    def right(self):
        """
        Moves the paddle right until it reaches the right wall.
        """
        if self.parts[len(self.parts)-1].xcor() < EDGE:
            for part in self.parts:
                part.forward(MOVE_DISTANCE)
