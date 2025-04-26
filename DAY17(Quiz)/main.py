from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

qus = []
for i in range(len(question_data)):
    qus.append(Question(question_data[i]["text"], question_data[i]["answer"]))

quiz = QuizBrain(qus)
while quiz.still_has_question():
    quiz.next_question()

print("You have Completed")
print(f"Your Score : {quiz.score}/{len(question_data)}")
