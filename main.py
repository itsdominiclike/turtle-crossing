import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from constants import HEIGHT, WIDTH, PLAYABLE_TOP, PLAYABLE_BOTTOM


player = Player()

# creating the lanes
def lanes():
    playable_bottom = PLAYABLE_BOTTOM
    lane = turtle.Turtle()
    lane.speed(0)
    lane.hideturtle()
    lane.penup()
    lane.pencolor("black")
    lane.left(180)
    while playable_bottom <= PLAYABLE_TOP:
        lane.goto(300, playable_bottom)
        for _ in range(30):
            lane.pendown()
            lane.forward(10)
            lane.penup()
            lane.forward(10)
        playable_bottom+=50




screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

lanes() # drawing lanes

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


