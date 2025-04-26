from turtle import Turtle

marked =[]

def check(name):
    if name in marked:
        return False
    else:
        marked.append(name)
        return True


class Mark(Turtle):
    def __init__(self, pos, name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(pos)
        self.pendown()
        self.write(f"{name}")

