from data import question_data
from quiz_brain import QuizBrain


class Question:
    def __init__(self, question, ans):
        self.que = question
        self.ans = ans


print("=" * 40)
print("      Welcome to the Quiz App!!")
print("-" * 40)
print(f"There are {len(question_data)} questions.")
print("Type 'True' or 'False' to answer each \nquestion.")
print("=" * 40)
print("\n")

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
