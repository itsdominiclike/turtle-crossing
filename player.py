from turtle import Turtle
from constants import STARTING_POSITION, MOVE_DISTANCE, FINISH_LINE_Y




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

    # current movement logic (stays in playable area - top of area is end of level)
    def move_up(self):
        if self.ycor() -300:
            self.start_y += MOVE_DISTANCE
            self.goto(self.start_x, self.start_y)

    def move_down(self):
        if self.ycor() > -280:
            self.start_y -= MOVE_DISTANCE
            self.goto(self.start_x, self.start_y)

    # def move_right(self):
    #     if self.xcor() < 250:
    #         self.start_x += MOVE_DISTANCE
    #         self.goto(self.start_x, self.start_y)
    #     elif 250 >= self.xcor() < 280:
    #         self.start_x += 20
    #         self.goto(self.start_x, self.start_y)

    # def move_left(self):
    #     if self.xcor() > -250:
    #         self.start_x -= MOVE_DISTANCE
    #         self.goto(self.start_x, self.start_y)
    #     elif -250 <= self.xcor() < -280:
    #         self.start_x -= 30
    #         self.goto(self.start_x, self.start_y)

    def move_right(self):
        if self.xcor() + MOVE_DISTANCE > 250:  # If the next move would go past 250
            self.start_x = 280  # Snap exactly to 280
        else:
            self.start_x += MOVE_DISTANCE
        self.goto(self.start_x, self.start_y)

    def move_left(self):
        if self.xcor() - MOVE_DISTANCE < -250:  # If the next move would go past -250
            self.start_x = -280  # Snap exactly to -280
        else:
            self.start_x -= MOVE_DISTANCE
        self.goto(self.start_x, self.start_y)

    def check_collision(self, car_list):
        for car in car_list:
            if self.distance(car) < 20:
                return True  # Collision detected
        return False  # No collision



