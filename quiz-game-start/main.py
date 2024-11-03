from question_model import Question
from data import question_data
from quiz_brain import QuizBrian
question_bank = []
for i in question_data:
    question = i["text"]
    answers = i["answer"]
    questions = Question(question,answers)
    question_bank.append(questions)
quiz = QuizBrian(question_bank)

while quiz.still_have_question():
    quiz.next_question()
print("yov'e completed Quiz ")
print(f"score was {quiz.scores}/12")