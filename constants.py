# Constants used throughout the Turtle Crossing game.

# Screen dimensions
HEIGHT = 600  # Height of the game window
WIDTH = 600   # Width of the game window

# Player settings
STARTING_POSITION = (0, -280)  # Initial position of the player at the bottom center
MOVE_DISTANCE = 25  # Distance the player moves per key press
FINISH_LINE_Y = 280  # Y-coordinate representing the finish line

# Car settings
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]  # Possible car colors
STARTING_MOVE_DISTANCE = 5  # Initial speed of cars
MOVE_INCREMENT = 10  # Speed increment per level
START_X = 320  # X-coordinate where cars start off-screen

# Playable area limits
PLAYABLE_TOP = HEIGHT / 2 - 50  # The highest y-coordinate cars can spawn
PLAYABLE_BOTTOM = -(HEIGHT / 2 - 50)  # The lowest y-coordinate cars can spawn

# Scoreboard font
FONT = ("Courier", 24, "normal")