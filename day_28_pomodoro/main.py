import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
t = None
mark = ""
# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global reps
    reps = 0
    canvas.after_cancel(t)
    canvas.itemconfig(timer, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start():
    global reps
    reps += 1
    ws = WORK_MIN * 60
    sb = SHORT_BREAK_MIN * 60
    lb = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_title.config(text="Break", fg=RED)
        count(lb)
    elif reps % 2 == 0:
        label_title.config(text="Break", fg=PINK)
        count(sb)
    else:
        count(ws)
        label_title.config(text="Work", fg=GREEN)

    # count(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import math


def count(n):
    global t
    minute = math.floor(n / 60)
    second = n % 60
    if second < 10:
        second = f"0{second}"
    if minute < 10:
        minute = f"0{minute}"
    canvas.itemconfig(timer, text=f"{minute}:{second}")
    if n > 0:
        t = window.after(5, count, n - 1)
    else:
        start()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


label_title = Label(text="Timer", font=(FONT_NAME, 50, "normal"), bg=YELLOW, fg=GREEN)
label_title.grid(row=0, column=1)

label_tick = Label(text=mark, font=("ariel", 20, "normal"), bg=YELLOW, fg=GREEN)
label_tick.grid(row=3, column=1)

start_butt = Button(text="Start", fg="blue", highlightthickness=0, command=start)
start_butt.grid(row=2, column=0)

reset_butt = Button(text="Reset", fg="blue", highlightthickness=0, command=reset)
reset_butt.grid(row=2, column=2)

window.mainloop()