from tkinter import *
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- WORDS -------------------------------#
with open("data/french_words.csv", "r") as file:
    data = pandas.read_csv(file)
    # data.to_dict()

def start_game():
    for (index, row) in data.iterrows():
        canvas.create_text(400, 150, text="French", fill=BACKGROUND_COLOR, font=("Ariel", 40, "italic"))
        canvas.create_text(400, 256, text=row.French, fill=BACKGROUND_COLOR, font=("Ariel", 40, "italic"))
        time.sleep(1)
        canvas.create_text(400, 150, text="English", fill=BACKGROUND_COLOR, font=("Ariel", 60, "bold"))
        canvas.create_text(400, 256, text=row.English, fill=BACKGROUND_COLOR, font=("Ariel", 40, "italic"))





# ------------------------------- UI SETUP ---------------------------- #

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

f_img = PhotoImage(file="images/card_front.png")
b_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263,  image=f_img)

canvas.create_text(400, 150, text="English", fill="black", font=("Ariel", 40, "bold"))
canvas.create_text(400, 256, text="row.English", fill="black", font=("Ariel", 60, "italic"))
time.sleep(1)
canvas.create_text(400, 150, text="Eng4454lish", fill="black", font=("Ariel", 40, "bold"))
canvas.create_text(400, 256, text="row.Engl111ish", fill="black", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# labels
# lang_label = Label(text="French", bg=BACKGROUND_COLOR, font=("Ariel", 40, "italic"))
# lang_label.place(x=400, y=150)
#
# word_label = Label(text="hi", bg=BACKGROUND_COLOR, font=("Ariel", 60, "bold"))
# word_label.place(x=400, y=263)




# buttons
w_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=w_img, highlightthickness=0, command=start_game)
wrong_button.grid(row=1, column=0)

r_img = PhotoImage(file="images/right.png")
right_button = Button(image=r_img, highlightthickness=0)
right_button.grid(row=1, column=1)




# lang_label.config(text="French")
# lang_label.place(x=400, y=150)
# time.sleep(3)
# lang_label.config(text="English")
# time.sleep(3)
# lang_label.config(text="French")
# start_game()

for (index, row) in data.iterrows():
    canvas.create_text(400, 150, text="French", fill=BACKGROUND_COLOR, font=("Ariel", 40, "italic"))
    canvas.create_text(400, 256, text=row.French, fill=BACKGROUND_COLOR, font=("Ariel", 40, "italic"))
    time.sleep(1)
    canvas.create_text(400, 150, text="English", fill=BACKGROUND_COLOR, font=("Ariel", 60, "bold"))
    canvas.create_text(400, 256, text=row.English, fill=BACKGROUND_COLOR, font=("Ariel", 40, "italic"))


window.mainloop()
