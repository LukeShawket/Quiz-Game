import question_model
import data
from question_model import Question
from quiz_brain import Brain
import ui

question_bank = []
data_dict = data.get_question("easy")

for key in data_dict:
    new_question = Question(data_dict[key]['question'], data_dict[key]['answer'])
    question_bank.append(new_question)

main_screen = ui.QuizUi(question_bank)