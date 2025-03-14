from turtle import Turtle
from constants import STARTING_POSITION, MOVE_DISTANCE, FINISH_LINE_Y

class Player(Turtle):
    """Player class that controls the turtle's movement in the game."""

    def __init__(self):
        """Initialize the player at the starting position."""
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.start_x = 0
        self.start_y = -280

    def move_up(self):
        """Move the player up if within bounds."""
        if self.ycor() < 280:  # Check if the player is below the top boundary
            self.start_y += MOVE_DISTANCE
            self.goto(self.start_x, self.start_y)

    def move_down(self):
        """Move the player down if within bounds."""
        if self.ycor() > -280:  # Check if the player is above the bottom boundary
            self.start_y -= MOVE_DISTANCE
            self.goto(self.start_x, self.start_y)

    def move_right(self):
        """Move the player right if within bounds."""
        if self.xcor() + MOVE_DISTANCE > 250:  # If the next move would go past 250
            self.start_x = 280  # Snap exactly to 280
        else:
            self.start_x += MOVE_DISTANCE
        self.goto(self.start_x, self.start_y)

    def move_left(self):
        """Move the player left if within bounds."""
        if self.xcor() - MOVE_DISTANCE < -250:  # If the next move would go past -250
            self.start_x = -280  # Snap exactly to -280
        else:
            self.start_x -= MOVE_DISTANCE
        self.goto(self.start_x, self.start_y)

    def check_collision(self, car_list):
        """Check for collision with a list of cars."""
        for car in car_list:
            if self.distance(car) < 20:
                return True
        return False

    def at_finish_line(self):
        """Check if the player has reached the finish line."""
        if self.ycor() >= FINISH_LINE_Y:
            self.go_to_start()
            return True
        return False

    def go_to_start(self):
        """Reset the player to the starting position."""
        self.start_x, self.start_y = STARTING_POSITION
        self.goto(STARTING_POSITION)
