from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.start_x = 0
        self.start_y = -280

    # current movement logic (added ability to also go down, left and right)
    def move_up(self):
        self.start_y += MOVE_DISTANCE
        self.goto(self.start_x, self.start_y)
    def move_down(self):
        self.start_y -= MOVE_DISTANCE
        self.goto(self.start_x, self.start_y)
    def move_right(self):
        self.start_x += MOVE_DISTANCE
        self.goto(self.start_x, self.start_y)
    def move_left(self):
        self.start_x -= MOVE_DISTANCE
        self.goto(self.start_x, self.start_y)