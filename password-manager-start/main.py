from tkinter import *
# * means import all classes from the pkg. messagebox is not a class here
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    shuffle(password_list)
    password_strong = "".join(password_list)

    password_entry.insert(0, string=password_strong)
    pyperclip.copy(password_strong)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        },
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"Below details are entered : \nEmail: {email} \nPassword: {password} \nIs is ok to save?")

        # if is_ok:
        # with open(file="data.txt", mode="w") as file:
        # file.write(f"{website} | {email} | {password}\n")
        try:
            with open(file="data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open(file="data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# -----------------------------FIND PASSWORD--------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open(file="data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title=website, message="No Data File Found")
    else:
        if website in data:
            account_details = data[website]
            email = account_details['email']
            password = account_details['password']
            messagebox.showinfo(title=website, message=f"Email : {email}\nPassword : {password}")
        else:
            messagebox.showinfo(title=website, message=f"No details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

logo_image = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", highlightthickness=0)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ", highlightthickness=0)
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ", highlightthickness=0)
password_label.grid(row=3, column=0)

website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, pady=2)
website_entry.focus()
email_entry = Entry(width=49)
email_entry.grid(row=2, column=1, columnspan=2, pady=2)
email_entry.insert(0, "ad.iemcal@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

generate_pass_button = Button(text="Generate Password", command=generate_password, width=15)
generate_pass_button.grid(row=3, column=2, pady=2)
add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=2)
search_button = Button(text="Search", command=find_password, width=15)
search_button.grid(row=1, column=2, pady=2)

screen.mainloop()
