from turtle import Turtle
import turtle
import random

a = Turtle()
turtle.colormode(255)
a.shape('turtle')
a.speed(15)
for i in range(360//5):
    b = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    a.color(b)
    a.circle(100)
    a.right(5)