from turtle import Turtle
from car_manager import CarManager

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-240, 270)
        self.color("Black")
        self.hideturtle()
        self.write(f"Level : {self.score}", align="center", font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        CarManager.update(self)
        self.write(f"Level : {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


