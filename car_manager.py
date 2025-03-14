import turtle
import random
from constants import COLORS, MOVE_INCREMENT, STARTING_MOVE_DISTANCE, PLAYABLE_TOP, PLAYABLE_BOTTOM

class CarManager:
    """Manages the creation, movement, and speed control of cars in the game."""

    def __init__(self):
        """Initializes the car manager with lane properties and speed settings."""
        self.x_start = 320  # Cars spawn off-screen from the right
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial speed of the cars
        self.lane_height = self.lanes(50)  # Defines lane height
        self.lane_centers = self.get_lane_center(self.lane_height)  # Get lane center positions
        self.cars = []  # List to store active car objects
        self.cars_to_remove = []  # List to store cars that need to be removed

    def create_car(self):
        """Creates a new car at a random lane position and adds it to the car list."""
        self.new_car = turtle.Turtle()
        self.new_car.penup()
        self.new_car.shapesize(1, 2, None)  # Set car dimensions
        self.new_car.shape('square')
        self.new_car.color(random.choice(COLORS))  # Assign a random color
        self.rand_y = random.choice(self.lane_centers)  # Assign random lane position
        self.new_car.goto(self.x_start, self.rand_y)  # Position the car at the start location
        self.cars.append(self.new_car)  # Add car to active car list

    def move(self):
        """Moves all cars to the left and removes cars that go off-screen."""
        for car in self.cars:
            new_x = car.xcor() - self.car_speed  # Move left by car_speed amount
            car.goto(new_x, car.ycor())

            # If the car moves off-screen, hide it and mark it for removal
            if car.xcor() < -320:
                car.hideturtle()
                self.cars_to_remove.append(car)

        # Remove cars that have moved off-screen from the main list
        for car in self.cars_to_remove:
            self.cars.remove(car)
        self.cars_to_remove.clear()  # Clear the removal list

    def speed_up(self):
        """Increases the speed of all cars by a fixed increment."""
        self.car_speed += MOVE_INCREMENT

    def lanes(self, lane_height):
        """Draws dashed lane dividers and returns the lane height.

        Args:
            lane_height (int): Height of each lane.

        Returns:
            int: The lane height used.
        """
        playable_bottom = PLAYABLE_BOTTOM
        lane = turtle.Turtle()
        lane.speed(0)
        lane.hideturtle()
        lane.penup()
        lane.pencolor("black")
        lane.left(180)

        # Draw dashed lines for lane dividers
        while playable_bottom <= PLAYABLE_TOP:
            lane.goto(300, playable_bottom)
            for _ in range(30):
                lane.pendown()
                lane.forward(10)
                lane.penup()
                lane.forward(10)
            playable_bottom += lane_height

        return lane_height

    def get_lane_center(self, lane_height):
        """Calculates and returns the center positions of each lane.

        Args:
            lane_height (int): Height of each lane.

        Returns:
            list: A list of y-coordinates for the center of each lane.
        """
        lane_centers = []
        current_lane = PLAYABLE_BOTTOM

        # Calculate lane centers while ensuring they don't exceed the playable area
        while current_lane < PLAYABLE_TOP:
            lane_center = current_lane + (lane_height / 2)
            if lane_center <= 250:
                lane_centers.append(lane_center)
                current_lane += lane_height
        return lane_centers
