class QuizBrain:
    score = 0
    def __init__(self,a):
        self.question_no = 0
        self.question_list = a

    def still_has_question(self):
        if self.question_no < len(self.question_list)-1:
            return True
        else:
            return False

    def next_question(self):
        self.question_no += 1
        choice = input(f"Q{self.question_no}. {self.question_list[self.question_no].text} (True/False)?")
        self.check_answer(choice, self.question_list[self.question_no].ans)

    def check_answer(self, a, b):
        if a == b:
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"Correct answer is {b}")
        print(f"Your Score is {self.score}/{self.question_no}\n\n")
