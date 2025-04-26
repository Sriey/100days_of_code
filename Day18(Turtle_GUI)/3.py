from turtle import Turtle
import random

a = Turtle()
a.shape('turtle')
for i in range(3, 11):
    for j in range(i):
        a.forward(100)
        a.right(360//i)

