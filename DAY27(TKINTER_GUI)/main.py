from tkinter import *

window = Tk()
window.minsize(width=500, height=500)
window.title("My First GUI Program")
window.config(padx=100,pady=100)

#LABEL
my_label = Label(text="TEXT")
my_label.grid(row=0,column=0)


#FUNCTION FOR BUTTON PRESS
def clicked():
    text = Input.get()
    my_label.config(text=text)
    my_label.grid(row=0,column=0)

#BUTTON
my_button = Button(text="Click Me", command=clicked)
my_button.grid(row=1,column=2)

#NEW_BUTTON
my_button = Button(text="Click Me", command=clicked)
my_button.grid(row=0,column=3)

#INPUT(ENTRY)
Input = Entry(width=10)
Input.grid(row=2,column=4)

window.mainloop()