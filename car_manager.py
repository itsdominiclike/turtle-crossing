from turtle import Turtle
import random
from constants import COLORS, MOVE_INCREMENT

class CarManager(Turtle):
    def __init__(self, y_pos):
        super().__init__()
        self.x_start = 320 # off screen, from the right
        self.y_pos = y_pos
        self.randcolor = random.choice(COLORS)
        self.create_car()
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        self.penup()
        self.shapesize(1,2,None)
        self.shape('square')
        self.color(self.randcolor)
        self.goto(self.x_start, self.y_pos)

    def speed_up(self, at_end):
        if at_end:
            self.car_speed += MOVE_INCREMENT

    def move(self):
        self.x_start-= self.car_speed
        self.goto(self.x_start, self.y_pos)





