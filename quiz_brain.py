
class Brain:
    def __init__(self, data):
        self.question_id = 0
        self.question_list = data
        self.score = 0

    def is_have_question(self):
        return self.question_id < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_id]
        self.question_id += 1
        user_input = input(f"Q.{self.question_id}: {current_question.text}(True/False):\n")
        self.analyze(current_question, user_input)

    def analyze(self, question, user_answer):
        right_answer = question.answer
        if right_answer == user_answer:
            self.score += 1
            print(f"Congratulations! Your answer is correct.\nYour current score is: {self.score}")
        else:
            print(f"Sorry! Your answer is incorrect.\nRight answer is {right_answer}")
