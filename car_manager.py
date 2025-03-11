from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, color, x_pos, y_pos):
        super().__init__()
        self.car_color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.create_car()

    def create_car(self):
        self.penup()
        self.shapesize(1,2,None)
        self.shape('square')
        self.color(self.car_color)
        self.goto(self.x_pos, self.y_pos)

