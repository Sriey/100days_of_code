from turtle import Turtle, Screen

a = Turtle()
b = Screen()
b.setup(width=500, height=400)
b.listen()


def m_f():
    a.forward(10)


def m_b():
    a.backward(10)


def c_c():
    a.left(15)


def a_c():
    a.right(15)


def clear():
    a.clear()
    a.penup()
    a.home()
    a.pendown()


b.onkeypress(m_f, "w")
b.onkeypress(m_b, "s")
b.onkeypress(a_c, "a")
b.onkeypress(c_c, "d")
b.onkeypress(clear, "c")

b.exitonclick()
