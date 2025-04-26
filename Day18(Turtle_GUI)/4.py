from turtle import Turtle
import random

a = Turtle()
a.shape('turtle')
b = ["red", "green", "blue", "black", "purple", "white", "yellow", "pink", "brown"]
c = [0, 90, 180, 270]
a.pensize(4)
a.speed("fastest")
for i in range(20):
    a.forward(30)
    a.setheading(random.choice(c))
    a.color(random.choice(b))
