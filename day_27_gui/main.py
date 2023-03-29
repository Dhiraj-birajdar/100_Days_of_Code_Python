from tkinter import *


def clicked():
    # my_label.config(text="Button got clicked!")
    txt = input.get()
    my_label.config(text=txt)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
# label
my_label = Label(text="My lable", font=("courier", 22))
my_label["text"] = "New Text"
my_label.config(text="New text")
my_label.grid(row=0, column=0)

# button
button = Button(text="Click Me", command=clicked)
button.grid(row=1, column=1)

# button
button = Button(text="New button", command=clicked)
button.grid(row=0, column=2)

# Entry
input = Entry(width=12)
print(input.get())
input.grid(row=2, column=3)

window.mainloop()
