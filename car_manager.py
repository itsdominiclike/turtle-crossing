from turtle import Turtle
import random

from main import HEIGHT

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_X = 320

PLAYABLE_TOP = HEIGHT/2
PLAYABLE_BOTTOM = (HEIGHT/2)*-1


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        # self.x_pos = x_pos
        # self.y_pos = y_pos
        self.create_car()
        self.randcolor = random.choice(COLORS)


    def create_car(self):
        self.penup()
        self.shapesize(1,2,None)
        self.shape('square')
        self.color(self.randcolor)


