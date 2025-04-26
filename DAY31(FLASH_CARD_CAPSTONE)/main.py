from tkinter import Tk, Canvas, PhotoImage, Button, Label
import random
import pandas

#----------------------------------------VARIABLE INITIALISATIONS------------------------------------------#

BACKGROUND_COLOR = "#B1DDC6"
Language_Font = ("Ariel",40,"italic")
Text_Font = ("Ariel",60,"bold")
word=""
fr_word = ""
a = ""
data = []

#----------------------------------------READING DATASETS--------------------------------------------------#
try:
    data = pandas.read_csv("data/To_Learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    eng = data["English"].to_list()
    fr = data["French"].to_list()

def time(count):
    global a
    if count < 1:
        window.after_cancel(a)
        timer = Label(text="  ", font=("Ariel", 50, "bold"), highlightthickness=0, bg=BACKGROUND_COLOR)
        timer.grid(row=1, column=1)
        back()
    else:
        timer = Label(text=count,font=("Ariel",50,"bold"),highlightthickness=0,bg=BACKGROUND_COLOR)
        timer.grid(row=1, column=1)
        a = window.after(1000, time,count-1)

def reset():
    window.after_cancel(a)
    front()

def front():
    time(3)
    global fr_word,word
    fr_word = random.choice(fr)
    word = eng[fr.index(fr_word)]
    canvas.create_image(400, 263, image=back_image)
    canvas.create_text(400, 150, text="French", font=Language_Font)
    canvas.create_text(400, 263, text=fr_word, font=Text_Font)

def back():
    global fr_word,word
    word = eng[fr.index(fr_word)]
    canvas.create_image(400, 263, image=front_image)
    canvas.create_text(400, 150, text="English", font=Language_Font)
    canvas.create_text(400, 263, text=word, font=Text_Font)

def correct():
    global fr,eng,fr_word,word
    fr.remove(fr_word)
    eng.remove(word)
    data_frame = {"French":fr,"English":eng}
    df = pandas.DataFrame(data_frame)
    df.to_csv("data/To_Learn.csv")
    reset()

#------------------------------------GUI INTERFACE------------------------------------------#

window = Tk()
window.title("Flash_Card")
window.minsize(width =900,height=600)
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_image = PhotoImage(file ="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas.grid(row=0,column=1)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right,bg=BACKGROUND_COLOR,highlightthickness=0,command=correct)
right_button.grid(row=1,column=1,sticky="e",padx=50)

cross = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross,bg=BACKGROUND_COLOR,highlightthickness=0,command=reset)
cross_button.grid(row=1,column=1,sticky="w",padx=50)

#--------------------------------------MAIN FUNCTION---------------------------------------------#

front()
window.mainloop()