from turtle import Turtle

a = Turtle()
a.pensize(1)
for i in range(10):
    if i % 2 == 0:
        a.pendown()
    else:
        a.penup()
    a.forward(10)