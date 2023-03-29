from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def pass_gen():

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)
    password = "".join(password_list)

    pass_input.delete(0, END)
    pass_input.insert(0, password)
    # copies password to clipboard
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_login():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    user_data = {website: {
        "Email": email,
        "Password": password,
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Field empty", message="Please fill out required fields.")
    else:
        # ans = messagebox.askokcancel(title=website, message=f"Confirm details : \nEmail: {email} \nPassword: {password}")
        # if ans:
        try:
            with open("login_data.json", "r") as file:
                # file.write(f"{website} | {email} | {password}\n")
                # reading data
                data = json.load(file)
        except FileNotFoundError:
            with open("login_data.json", "w") as file:
                json.dump(user_data, file, indent=4)
        else:
            # updating data
            data.update(user_data)
            with open("login_data.json", "w") as file:
                # writing data
                json.dump(data, file, indent=4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)
# ---------------------------- SEARCH PASSWORD -------------------------#


def search():
    website = web_input.get().title()
    try:
        with open("login_data.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops!", message="Database is not available")
    else:
        if website in data:
            msg = f"Email: {data[website]['Email']} \nPassword: {data[website]['Password']}"
            messagebox.showinfo(title=website, message=msg)
        else:
            messagebox.showerror(title="Oops!", message="Login info not found in database.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("MyPass: Password Manager")
window.config(padx=50, pady=50)


# canvas/ logo
logo = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=img)
logo.grid(row=0, column=1)


# input field
web_input = Entry(width=22)
web_input.focus()
web_input.grid(row=1, column=1)

email_input = Entry(width=41)
email_input.insert(0, "dhiraj@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

pass_input = Entry(width=20)
pass_input.grid(row=3, column=1)


# buttons
search_button = Button(text="Search", command=search, width=10)
search_button.grid(row=1, column=2)

gen_pass_button = Button(text="Generate Password", command=pass_gen)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=35, command=save_login)
add_button.grid(row=4, column=1, columnspan=2)


# labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/UserName:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)


window.mainloop()
