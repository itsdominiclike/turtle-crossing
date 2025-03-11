import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

HEIGHT = 600
WIDTH = 600

player = Player()


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

# basic key input listener - can make it similar to the pong game if needed
screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car = CarManager()

