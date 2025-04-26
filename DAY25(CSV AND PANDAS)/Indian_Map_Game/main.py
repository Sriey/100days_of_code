from turtle import Screen
from Check_mark import check, Mark, marked
import pandas

screen = Screen()
screen.title("India State's Game")
screen.bgpic("blank_states_img.gif")

game_is_on = True
score = 0

while game_is_on:
    Entry = screen.textinput(f"{score}/28 Guess The State", "Enter The Name Of The State.")
    states = pandas.read_csv("states_coords.csv")
    if Entry.title() == "Exit":
        state = [x for x in states["state"] if x not in marked]
        print(state)
        break
    if any(states.state == Entry.title()):
        temp = states[states.state == Entry.title()]
        x = int(temp.x.item())
        y = int(temp.y.item())
        if check(Entry):
            score += 1
            Mark((x, y), Entry)
    if score >= 28:
        game_is_on = False

screen.exitonclick()

