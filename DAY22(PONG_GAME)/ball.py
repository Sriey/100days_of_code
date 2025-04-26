from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, a):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=0.7,  stretch_len=0.7)
        self.setheading(random.choice([0, 180]))
        self.speed(a)

    def move(self, x, y, a):
        self.speed(a)
        self.goto(x=self.xcor()+x, y=self.ycor()+y)
