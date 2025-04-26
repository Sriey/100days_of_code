from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_after = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_after)
    timer_label.config(text="TIMER")
    canvas.itemconfig(timer, text=f"00:00")
    check_mark_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_down():
    global reps
    reps += 1
    if reps % 2 != 0:
        timer_label.config(text="WORK TIME",fg=PINK)
        count_down(WORK_MIN*60)
    else:
        if reps % 8 != 0:
            timer_label.config(text="SHORT BREAK",fg=RED)
            count_down(SHORT_BREAK_MIN * 60)
        else:
            timer_label.config(text="LONG BREAK",fg=GREEN)
            count_down(LONG_BREAK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    if 0 <= count_min < 10:
        count_min = "0" + str(count_min)
    count_sec = count % 60
    if 0 <= count_sec < 10 :
        count_sec = "0" + str(count_sec)
    if int(count_min) >= 0:
        canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
        global my_after
        my_after = window.after(1000,count_down,count-1)
    else:
        window.attributes('-topmost', True)
        window.attributes('-topmost',False)
        global reps
        print (reps)
        if reps % 2 != 0:
            mark = "".join( ["✔" for _ in range(int(reps/2)+1)])
            check_mark_label.config(text=mark)
        timer_down()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.wm_attributes('-toolwindow', 'true')
window.config(padx=100,pady=50,bg=YELLOW)

timer_label = Label(text = "TIMER",fg=GREEN,font=(FONT_NAME,30,"bold"),bg=YELLOW)
timer_label.grid(row=0,column=1)

reset_button = Button(text="RESET",command=reset_timer)
reset_button.grid(row=2,column=2)

start_button = Button(text="START",command = timer_down)
start_button.grid(row=2,column=0)

check_mark_label = Label(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,10,"bold"))
check_mark_label.grid(row=3,column=1)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image)
timer = canvas.create_text(100, 130,text="00:00",fill="White",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

window.mainloop()
