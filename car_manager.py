from turtle import Turtle
import random
from constants import HEIGHT, COLORS, STARTING_MOVE_DISTANCE, MOVE_INCREMENT, START_X, PLAYABLE_TOP, PLAYABLE_BOTTOM



class CarManager(Turtle):
    def __init__(self, y_pos):
        super().__init__()
        self.x_start = 320 # off screen, from the right
        self.y_pos = y_pos
        self.randcolor = random.choice(COLORS)
        self.create_car()


    def create_car(self):
        self.penup()
        self.shapesize(1,2,None)
        self.shape('square')
        self.color(self.randcolor)
        self.goto(self.x_start, self.y_pos)

    def move(self):
        self.x_start-=MOVE_INCREMENT
        self.goto(self.x_start, self.y_pos)




