from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorebord import Score
from wall import Wall
import time

speed = 1

screen = Screen()
screen.listen()
screen.title("Pong Game")
screen.tracer(0)
screen.setup(width=1000, height=600)
screen.bgcolor("black")

# Making middle wall
wall = Wall()

# Making Right Paddle
left_bat = Paddle((-480, 0))
screen.onkey(left_bat.up, "w")
screen.onkey(left_bat.down, "s")
right_score = Score((-50, 260))

# Making Left Paddle
right_bat = Paddle((472.50, 0))
screen.onkey(right_bat.up, "Up")
screen.onkey(right_bat.down, "Down")
left_score = Score((50, 260))

# Make Ball
ball = Ball(speed)
screen.update()
screen.tracer(1)

x = 10
y = 10
game_is_on = True
while game_is_on:
    if 290 <= ball.ycor() or ball.ycor() <= -290:
        y *= -1
    if ball.distance(right_bat) < 30 and ball.xcor() >= 465 or ball.distance(left_bat) < 30 and ball.xcor() <= -465:
        speed = speed + 1
        ball.speed(speed + 1)
        x *= -1
    if ball.xcor() > 480:
        ball.teleport(0, 0)
        speed = 1
        time.sleep(1)
        right_score.count()
        x *= -1
    if ball.xcor() < -480:
        ball.teleport(0, 0)
        left_score.count()
        speed = 1
        time.sleep(1)
        x *= -1
    ball.move(x, y, speed)


screen.exitonclick()
