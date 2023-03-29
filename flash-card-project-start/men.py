from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
# -------------------------------------------
card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/to_learn.csv")
    # data = {row.French: row.English for (index, row) in data.iterrows()}
    # f_words = [data[k] for (k, v) in data.items()]
except FileNotFoundError:
    org_data = pandas.read_csv("data/french_words.csv")
    to_learn = org_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def word():
    global card, timer
    window.after_cancel(timer)
    card = choice(to_learn)
    canvas.itemconfig(c_title, text="French", fill="black")
    canvas.itemconfig(c_word, text=card["French"], fill="black")
    canvas.itemconfig(c_img, image=f_img)
    timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(c_title, text="English", fill="white")
    canvas.itemconfig(c_word, text=card["English"], fill="white")
    canvas.itemconfig(c_img, image=b_img)


def known_word():
    to_learn.remove(card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/to_learn.csv", index=False)
    word()

    
# -------------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526)
f_img = PhotoImage(file="images/card_front.png")
b_img = PhotoImage(file="images/card_back.png")
c_img = canvas.create_image(400, 263, image=f_img)
c_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
c_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

w_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=w_img, highlightthickness=0, command=word)
wrong_button.grid(row=1, column=0)

r_img = PhotoImage(file="images/right.png")
right_button = Button(image=r_img, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=1)

# for i in range(10):
#     card = choice(words)
#     canvas.itemconfig(c_title, text="French")
#     canvas.itemconfig(c_word, text=card["French"])
#     canvas.itemconfig(c_img, image=b_img)
#     time.sleep(3)
#     canvas.itemconfig(c_title, text="English")
#     canvas.itemconfig(c_word, text=card["English"])
#     canvas.itemconfig(c_img, image=f_img)
word()
window.mainloop()