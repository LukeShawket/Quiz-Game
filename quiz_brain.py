import html

class Brain:
    def __init__(self, data):
        self.question_id = 0
        self.question_list = data
        self.score = 0
        self.current_question = ""
        self.true_answer = ""
        self.true_text = "Congratulations! Your answer is correct."
        self.false_text = "Sorry! Your answer is incorrect."
        self.result = ""

    def is_have_question(self):
        return self.question_id < len(self.question_list)

    def get_question(self):
        if self.is_have_question():
            self.current_question = html.unescape(self.question_list[self.question_id].text)
            self.true_answer = html.unescape(self.question_list[self.question_id].answer).lower()
        else:
            self.current_question = ""
            self.true_answer = ""
        # print(self.question_id)
        # print(self.current_question)
        # print(self.true_answer)
        return self.current_question
    
    def next_question(self):
        self.question_id += 1

    def analyze(self, user_answer):
        if self.true_answer == user_answer:
            self.score += 1
            self.result = self.true_text
        else:
            self.result = self.false_text
        return self.result
            
