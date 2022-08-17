from turtle import Turtle
import sys
import os

# CONSTANTS
ALIGNMENT = "left"
FONT = ("Arial", 16, 'bold')
FAIL_FONT = ("Arial", 30, 'bold')

color_scales = {
    "green": 1,
    "yellow": 2,
    "orange": 5,
    "red": 8
}


def resource_path(relative_path):
    """ Get the absolute path to the resource.
    (borrowed from Stackoverflow: https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile) """
    try:
        # Pyinstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Getting previous top-score
with open(resource_path("topscore.txt"), "r") as file:
    top = int(file.read())


class Scoreboard(Turtle):
    """
    Scoreboard class inherits from the Turtle class and is used to create the scoreboard that tracks and updates
    player's score and lives.

    Methods:
        __init__(self)
        update_scoreboard(self)
        add_point(self)
        lose_life(self)
        game_over(self)
    """

    def __init__(self):
        super().__init__()
        """
        Scoreboard class constructor to initialize the object.
        """

        # Initial attributes
        self.score = 0
        self.top_score = top
        self.lives = 5

        # Initial turtle settings
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(-430, 290)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the current score and number of lives left.
        """

        self.goto(-430, 290)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.goto(300, 290)
        self.write(f"{self.lives * ' ❤'}", False, align=ALIGNMENT, font=FONT)

    def add_point(self, color_scale):
        """
        Increments score based on the color of the brick player has hit. Updates top score if current score has
        surpassed it. Calls update_scoreboard method.
        :param color_scale: dictionary of color-keys and their associated point-scaling value
        """
        self.clear()
        self.score += color_scales[color_scale]
        if self.score > self.top_score:
            self.top_score = self.score
            with open(resource_path("topscore.txt"), "w") as score_file:
                score_file.write(str(self.top_score))
        self.update_scoreboard()

    def lose_life(self):
        """
        Removes a life from player's remaining lives. Calls update_scoreboard method.
        """
        self.clear()
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self, message):
        """
        Displays game-over message with player's score and the top score.
        :param message: End-game message, as a string.
        """

        self.clear()
        self.goto(-120, -50)
        self.write(f"{message}", align=ALIGNMENT, font=FAIL_FONT)
        self.goto(-80, -100)
        self.write(f"Top Score: {self.top_score}", False, align=ALIGNMENT, font=FONT)
        self.goto(-75, -150)
        self.write(f"Your Score: {self.score}", False, align=ALIGNMENT, font=FONT)
