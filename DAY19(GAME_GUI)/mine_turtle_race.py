from turtle import Turtle, Screen
import random
tim = [0, 1, 2, 3, 4]
colour = ["red", "blue", "green", "yellow", "purple"]
c = 200
screen = Screen()
screen.setup(width=630, height=450)
user_input = screen.textinput(title="User Bet", prompt="Choose between red blue,green,yellow,purple")

for i in range(5):
    tim[i] = Turtle()
    tim[i].shape("turtle")
    tim[i].penup()
    tim[i].color(colour[i])
    tim[i].goto(-300, c)
    c -= 100
tim[0].speed("fastest")
tim[1].speed("fastest")
tim[2].speed("fastest")
tim[3].speed("fastest")
tim[4].speed("fastest")
d = 0

while 1:
    tim[0].forward(random.randint(0, 10))
    tim[1].forward(random.randint(0, 10))
    tim[2].forward(random.randint(0, 10))
    tim[3].forward(random.randint(0, 10))
    tim[4].forward(random.randint(0, 10))
    for i in range(5):
        if int(tim[i].xcor()) >= 300:
            if tim[i].pencolor() == user_input:
                print("You Won")
            else:
                print(f"You Lose,The Winner was {tim[i].pencolor()}")
            d = 1
    if d == 1:
        break

screen.exitonclick()