from tkinter import *
from PIL import Image, ImageTk
import quiz_brain
import data
from question_model import Question

class QuizUi():
    def __init__(self, data):

        self.brain = quiz_brain.Brain(data=data)
        if self.brain.is_have_question():
            self.current_question = self.brain.get_question()

        self.window = Tk()
        self.window.title("Quiz Master")
        self.window.config(bg='#898121',padx=50, pady=50)
        self.window.geometry("400x700")
        self.score_label = Label(text=f"Score: {self.brain.score}", bg="#898121", fg="white", font=('Arial', 20, 'bold'))
        self.score_label.grid(row=0, column=0, sticky='nw')

        canvas_image_source = Image.open("canvas_image.png")
        resized_canvas_image = canvas_image_source.resize((300, 300))
        canvas_image = ImageTk.PhotoImage(resized_canvas_image)

        self.canvas = Canvas(width=300, height=300, highlightthickness=0)
        self.canvas.create_image(150, 150, image=canvas_image)
        self.question_text = self.canvas.create_text(150, 150, text=f"Q.{self.brain.question_id+1}: {self.current_question}", fill='white', font=('Arial', 15, 'italic'), width= 280)
        self.canvas.grid(row=1, column=0, columnspan=3, pady=50)

        true_image_source = Image.open("true.png")
        false_image_source = Image.open("false.png")
        resized_true = true_image_source.resize((100, 100))
        resized_false = false_image_source.resize((100, 100))
        self.true_image = ImageTk.PhotoImage(resized_true)
        self.false_image = ImageTk.PhotoImage(resized_false)
        self.false_button = Button(image=self.false_image, highlightthickness=0,borderwidth=0, relief='flat', command=self.set_user_answer_false)
        self.false_button.grid(row=3, column=0, pady=20)
        self.true_button = Button(image=self.true_image, highlightthickness=0, borderwidth=0, relief='flat', command=self.set_user_answer_true)
        self.true_button.grid(row=3, column=2, pady=20)

        interactive_source = Image.open("interactive.png")
        resized_interactive = interactive_source.resize((300, 100))
        self.interactive_image = ImageTk.PhotoImage(resized_interactive)
        self.interact_button = Button(image=self.interactive_image, compound="center", fg="white", font=('Arial', 20, 'bold'), 
                                      borderwidth=0, highlightthickness=0, relief='flat', padx=0, pady=0)

        self.window.mainloop()

    def set_user_answer_true(self):
        self.brain.next_question()
        self.false_button.grid_forget()
        self.true_button.grid_forget()
        self.interact_button.config(text="Next", command=self.next_button)
        self.interact_button.grid(row=3, column=0, columnspan=3, pady=20)
        result = self.brain.analyze("true")
        self.canvas.itemconfig(self.question_text, text=f"{result}")
        self.score_label.config(text=f"Score: {self.brain.score}")

    def set_user_answer_false(self):
        self.brain.next_question()
        self.false_button.grid_forget()
        self.true_button.grid_forget()
        self.interact_button.config(text="Next", command=self.next_button)
        self.interact_button.grid(row=3, column=0, columnspan=3, pady=20)
        result = self.brain.analyze("false")
        self.canvas.itemconfig(self.question_text, text=f"{result}")
        self.score_label.config(text=f"Score: {self.brain.score}")

    def next_button(self):
        
        if self.brain.is_have_question():
            self.interact_button.grid_forget()
            self.false_button.grid(row=3, column=0)
            self.true_button.grid(row=3, column=2)
            self.current_question = self.brain.get_question()
            self.canvas.itemconfig(self.question_text, text=f"Q.{self.brain.question_id+1}: {self.current_question}")
        else:
            self.canvas.itemconfig(self.question_text, text=f"      Game Over!\nYour final score is {self.brain.score}")
            self.false_button.grid_forget()
            self.true_button.grid_forget()
            self.interact_button.config(text="Play Again", command=self.play_again)
            self.interact_button.grid(row=3, column=0, columnspan=3, pady=20)

    def play_again(self):
        self.interact_button.grid_forget()
        question_data = data.get_question('easy')
        question_list = []
        for key in question_data:
            new_question = Question(question_data[key]['question'], question_data[key]['answer'])
            question_list.append(new_question)
        self.brain.question_list = question_list
        self.brain.question_id = 0
        self.false_button.grid(row=3, column=0)
        self.true_button.grid(row=3, column=2)
        self.brain.score = 0
        self.score_label.config(text=f"Score: {self.brain.score}")
        if self.brain.is_have_question():
            self.current_question = self.brain.get_question()
        self.canvas.itemconfig(self.question_text, text=f"Q.{self.brain.question_id+1}: {self.current_question}")

