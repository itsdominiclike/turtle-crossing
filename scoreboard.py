from turtle import Turtle
from constants import FONT

class Scoreboard(Turtle):
    """Manages the scoreboard for the game, tracking levels and displaying messages."""

    def __init__(self):
        """Initializes the scoreboard, sets level to 1, and displays the initial level."""
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor('black')
        self.level = 1
        self.goto(-230, 260)  # Positioning the scoreboard on the screen
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def update_scoreboard(self):
        """Clears the current level display, increments the level, and updates the screen."""
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def game_over(self):
        """Displays the game over message at the center of the screen."""
        self.goto(0, 0)
        self.write("Game Over.", align='center', font=FONT)