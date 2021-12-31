from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        # Window config
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.config(bg=THEME_COLOR)
        self.window.minsize(width=340, height=500)
        self.window.maxsize(width=340, height=500)

        # Canvas
        self.canvas = Canvas()
        self.canvas.config(bg="white", height=250, width=300, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 120, width=250, font=("Arial", 15, "italic"))
        self.canvas.itemconfig(self.question_text, text="Question Text.")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(0, 40), padx=20)

        # Label
        self.score = Label()
        self.score.config(bg=THEME_COLOR, fg="white", pady=30)
        self.score.grid(row=0, column=1)

        # Button
        v_img = PhotoImage(file="images/true.png")
        self.v_button = Button(image=v_img, bg=THEME_COLOR, border=0,
                               activebackground=THEME_COLOR, command=self.its_true)
        self.v_button.grid(row=2, column=0)

        x_img = PhotoImage(file="images/false.png")
        self.x_button = Button(image=x_img, bg=THEME_COLOR, border=0,
                               activebackground=THEME_COLOR, command=self.its_false)
        self.x_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="There are no more questions!")
            self.v_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def its_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def its_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


