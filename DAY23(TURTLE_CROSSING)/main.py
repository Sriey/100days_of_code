import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

timmy = Player()
score = Scoreboard()
screen.onkey(timmy.go_up, 'Up')

game_is_on = True
car = []

while game_is_on:
    if 1 == random.randint(1, 6):
        temp = CarManager()
        car.append(temp)
    for a in car:
        a.move_car()

    time.sleep(0.1)
    screen.update()

    for a in car:
        if timmy.distance(a) < 30:
            score.game_over()
            game_is_on = False

    if timmy.check(score):
        for a in car:
            a.hideturtle()
        car = []
        timmy.reset()

screen.exitonclick()
