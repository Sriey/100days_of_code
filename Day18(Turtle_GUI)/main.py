from extracting_colour import a
from turtle import Turtle, Screen
import turtle
import random
turtle.colormode(255)
t = Turtle()
t.hideturtle()
t.penup()
b = -300
c = -300
for i in range(10):
    c = c + 50
    t.goto(b, c)
    for j in range(10):
        t.dot(10,random.choice(a))
        t.forward(50)

screen = Screen()
screen.exitonclick()