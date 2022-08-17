from turtle import Turtle

# Screen size constants
WIDTH = 900
HEIGHT = 700


class BrickManager:
    """
    BrickManager class is used to create, destroy, and keep track of all the colored bricks the player must break with
    the ball and paddle.

    Methods:
        __init__(self)
        create_wall(self)
        create_brick(self)
        remove_brick(self)
    """

    def __init__(self):
        """
        BrickManager class constructor to initialize the object.
        """
        # Brick colors
        self.colors = ["red", "red", "orange", "orange", "yellow", "yellow", "green", "green"]

        # To store reference to all bricks
        self.bricks = []

        # Creating all bricks
        self.create_wall()

    def create_wall(self):
        """
        Creates a wall made up of rows of colored bricks
        """

        # brick-placement cursor
        bx = -((WIDTH / 2) + 10)
        # row-placement cursor
        by = (HEIGHT/2) - 90

        # Creates a row of 10 bricks per color in self.colors
        for color in self.colors:
            for x in range(10):
                self.create_brick(color, bx, by)
                bx += 90
            # resetting brick-cursor to leftmost position on screen
            bx = -((WIDTH / 2) + 10)
            # dropping row-cursor down screen
            by = by - 30

    def create_brick(self, color, brick_x, brick_y):
        """
        Creates a row of 4 turtles directly next to each other. Appends 4-turtle collection (brick) to self.bricks to
        keep reference of them.
        :param color: The color of the brick, passed as a string.
        :param brick_x: X position on screen to draw turtle, as integer.
        :param brick_y: Y position on screen to draw turtle, as integer.
        """

        brick = []
        for x in range(4):
            brick_x += 20
            chunk = Turtle(shape="square")
            chunk.color(color)
            chunk.penup()
            chunk.goto((brick_x, brick_y))
            brick.append(chunk)

        self.bricks.append(brick)

    def remove_brick(self, to_destroy):
        """
        Removes a single brick from the wall.
        :param to_destroy: The brick to be destroyed, a collection of references to the individual turtles that make up
        the single brick.
        """

        for chunk in to_destroy:
            # must move chunk off-screen, as clear() only destroys reference to it
            chunk.goto(1000, 1000)
            chunk.clear()
        self.bricks.remove(to_destroy)


