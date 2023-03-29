from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizGui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250,bg="white")
        self.qn = self.canvas.create_text(150, 125, text="question", width=280, fill="black", font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = Label(text="Score: 0", foreground="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        t_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=t_img, highlightthickness=0, command=self.chk_ans_true)
        self.true_button.grid(row=2, column=0)

        f_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=f_img, highlightthickness=0, command=self.chk_ans_false)
        self.false_button.grid(row=2, column=1)

        self.next_qn()

        self.window.mainloop()

    def next_qn(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            qn_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.qn, text=qn_txt)
        else:
            self.canvas.itemconfig(self.qn, text="You have reached the end of quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def chk_ans_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def chk_ans_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.next_qn)

