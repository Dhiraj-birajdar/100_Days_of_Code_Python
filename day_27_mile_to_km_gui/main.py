from tkinter import *

window = Tk()
window.title("Mile to Kilo Meter converter")
# window.minsize(width=300, height=200)
window.config(padx=20, pady=20)


def calc():
    mile = float(entry.get())
    km = mile * 1.609344
    label3.config(text=round(km, 2))


# Entry
entry = Entry(width=10)
entry.get()
entry.focus()
entry.grid(row=0, column=1)

# Label
label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="0")
label3.grid(row=1, column=1)

label4 = Label(text="Km")
label4.grid(row=1, column=2)

# Button
button = Button(text="Calculate", command=calc)
button.grid(row=2, column=1)


window.mainloop()