import time
import turtle
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from constants import HEIGHT, WIDTH, PLAYABLE_TOP, PLAYABLE_BOTTOM, FINISH_LINE_Y, STARTING_POSITION, MOVE_INCREMENT

player = Player()
scoreboard = Scoreboard()

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
# screen.onkeypress(lambda: player.move_up(cars), "Up")
# screen.onkeypress(lambda: player.move_down(cars), "Down")
# screen.onkeypress(lambda: player.move_left(cars), "Left")
# screen.onkeypress(lambda: player.move_right(cars), "Right")
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


    for car in cars: # moving each car in list
        car.move()
    # new car very 5th loop
    if loop_counter % 5 == 0: # if there's been 5 loops
        rand_y = random.choice(lane_centers) #new random position for car to be in
        new_car = CarManager(rand_y) # new car
        cars.append(new_car) # adding new car to list of cars

    # car collision detection
    if player.check_collision(cars):
        # game_is_on = False
        screen.update()
        scoreboard.game_over()
        game_is_on=False

    # need to put player back to start, make cars faster and increase level by 1
    if player.ycor() > 280:
        player.goto(STARTING_POSITION)
        scoreboard.update_scoreboard()
        MOVE_INCREMENT+=1




    loop_counter +=1
screen.exitonclick()

