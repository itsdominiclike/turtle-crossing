from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor('black')
        self.level = 1
        self.goto(-230, 260)
        self.write(f"Level: {self.level}", align='center', font=FONT)


    def update_scoreboard(self):
        self.clear()
        self.level +=1
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over.", align='center', font= FONT)