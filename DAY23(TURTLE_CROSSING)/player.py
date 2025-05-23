from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.position = STARTING_POSITION
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def check(self, score):
        if self.ycor() >= FINISH_LINE_Y:
            score.update()
            return True
        else:
            return False

    def reset(self):
        self.goto(STARTING_POSITION)




