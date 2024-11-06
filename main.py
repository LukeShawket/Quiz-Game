import question_model
from data import question_data
from question_model import Question
from quiz_brain import Brain

question_bank = []
for question in question_data:
    new_question  = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = Brain(question_bank)

while quiz.is_have_question():
    quiz.next_question()