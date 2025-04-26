from logging import disable
from tkinter import Tk, Canvas, Label, Button, PhotoImage

THEME_COLOR = "#375362"
font=("Arial",20)

class UserInterface:
    def __init__(self, quiz):
        self.quiz = quiz
        self.window = Tk()
        self.window.minsize(width=600, height=500)
        self.window.title("Trivia Quiz")
        self.window.config(padx=50,pady=20,background=THEME_COLOR)

        self.score = Label(text="Score:0",background=THEME_COLOR,fg="White",font=font)
        self.score.grid(row=0,column=2,sticky="e")

        self.canvas = Canvas(width=550,height=250,highlightthickness=0)
        self.canvas.grid(row=1,column=0,columnspan=3,pady=30)
        self.text = self.canvas.create_text(275,125,width=530,text="Something",font=font,fill=THEME_COLOR)

        true_image = PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_image,highlightthickness=0,bg=THEME_COLOR,command=self.check_true)
        self.true_button.grid(row=2,column=0,rowspan=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button=Button(image=false_image,highlightthickness=0,bg=THEME_COLOR,command=self.check_false)
        self.false_button.grid(row=2,column=2)

        self.change_text()

        self.window.mainloop()

    def change_text(self):
        if self.quiz.question_number < len(self.quiz.question_list):
            question = self.quiz.next_question()
            self.score.config(text=f"Score : {self.quiz.score}")
            self.canvas.config(bg="White")
            self.canvas.itemconfig(self.text,text=question)
        else:
            self.canvas.config(bg="White")
            self.canvas.itemconfig(self.text, text="You Have Reached The End Of The Quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        self.change_score(self.quiz.check_answer(user_answer="True"))

    def check_false(self):
        self.change_score(self.quiz.check_answer(user_answer="False"))

    def change_score(self,check):
        if check:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500,self.change_text)
