from data import question_data
from quiz_brain import QuizBrain


class Question:
    def __init__(self, question, ans):
        self.que = question
        self.ans = ans


question_bank = []
for i in range(0, len(question_data)):
    q = question_data[i]["question"]
    a = question_data[i]["correct_answer"]
    question_bank.append(Question(q, a))


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.askque()

print("You completed the quiz !!")
print(f"Final score: {quiz.score}/{len(question_bank)}")
