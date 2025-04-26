from tkinter import *

window = Tk()
window.minsize(width=200,height=200)
window.title("MILES TO KILOMETER CONVERTER")
window.config(padx=30,pady=30)

Input = Entry(width=10)
Input.grid(row=0,column=1)

miles = Label(text="MILES")
miles.config(padx=5,pady=5)
miles.grid(row=0,column=2)

equal = Label(text="Is Equal To")
equal.config(padx=5,pady=5)
equal.grid(row=1,column=0)

km = Label(text="Km")
km.config(padx=5,pady=5)
km.grid(row=1,column=2)

def cal():
    mile = round(int(Input.get()) * 1.60934, 2)
    k = Label(text=f"{mile}")
    k.config(padx=5, pady=5)
    k.grid(row=1, column=1)

calculate = Button(text="Calculate",command=cal)
calculate.grid(row=2,column=1)

window.mainloop()