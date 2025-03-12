import time
import turtle
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from constants import HEIGHT, WIDTH, PLAYABLE_TOP, PLAYABLE_BOTTOM, FINISH_LINE_Y, STARTING_POSITION

player = Player()

# may be a good idea to put the bottom two functions inside of car_manager
# creating the lanes
def lanes(lane_height):
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
        playable_bottom+=lane_height
    return lane_height
# finds the center of the lanes, appends Y coordinate to list
def get_lane_center(lane_height):
    lane_centers = []
    current_lane = PLAYABLE_BOTTOM
    while current_lane < PLAYABLE_TOP:
        lane_center = current_lane+(lane_height/2)
        if lane_center <= 250:
            lane_centers.append(lane_center)
            current_lane+= lane_height
    return lane_centers


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

lane_height = lanes(50) # drawing lanes, returning lane_height for later use
lane_centers = get_lane_center(lane_height)


# random y position from lane_centers list
# rand_y = random.choice(lane_centers)


# basic key input listener - can make it similar to the pong game if needed
screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")


# car = CarManager(rand_y)
loop_counter = 0
cars = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    if loop_counter % 6 == 0: #creates a new car every 6 times the loop runs
        rand_y = random.choice(lane_centers)
        new_car = CarManager(rand_y)
        cars.append(new_car)

    for i in cars:
        i.move()# moves car - only until a new car is created


#   detect if turtle collides with car - sometimes it looks like they don't collide (the next key press would cause collision)
#     if player.distance(new_car) < 20: #not great currently as new_car constantly becomes a new car
#         game_is_on = False

    loop_counter +=1





screen.exitonclick()

