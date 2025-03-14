import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from constants import HEIGHT, WIDTH
"""
Main module for the Turtle Crossing game.
This module sets up the game, initializes objects, and runs the main game loop.
"""
## Setup game parameters
# Interval at which new cars are spawned
car_spawn_interval = 6
loop_counter = 0

# Game state
game_is_on = True

# Initialize objects
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)  # Disable automatic updates for smoother animations

player = Player()  # The player's turtle character
scoreboard = Scoreboard()  # Score tracking
new_car = CarManager()  # Handles all car-related logic

# Key input listener
screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")


# Main game loop
while game_is_on:
    time.sleep(0.1)  # Slows down the loop for better gameplay pacing
    screen.update()  # Refresh screen

    # Spawn a new car every `car_spawn_interval` loops
    if loop_counter % car_spawn_interval == 0:
        new_car.create_car()

    # Move all cars
    new_car.move()

    # Check if player reaches the finish line
    if player.at_finish_line():
        scoreboard.update_scoreboard()  # Increase score
        new_car.speed_up()  # Increase car speed

        # Reduce spawn interval (min 1) to increase difficulty
        if car_spawn_interval > 1:
            car_spawn_interval -= 1

    # Collision detection: if player collides with a car, game over
    if player.check_collision(new_car.cars):
        screen.update()
        scoreboard.game_over()
        game_is_on = False

    loop_counter += 1  # Track number of game loops
screen.exitonclick()  # Keep window open after game ends
