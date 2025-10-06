import tkinter
from tkinter import PhotoImage, END, messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for i in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if password == "" or website =="":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json","r") as pwd_file:
                data = json.load(pwd_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json","w") as pwd_file:
                json.dump(new_data, pwd_file, indent=4)
        else:

            with open("data.json", "w") as pwd_file:
                json.dump(data, pwd_file, indent=4)
        finally:
            entry_website.delete(0,END)
            entry_password.delete(0,END)
# ---------------------------- SEARCH---------------------------------- #
def find_password():
    website = entry_website.get()
    try:
        with open("data.json","r") as pwd_file:
            data = json.load(pwd_file)
    except FileNotFoundError:
        messagebox.showinfo(title="File not found", message="No Data File Found")
    else:
        if website in data:
            information = data[website]
            messagebox.showinfo(title="Username and Email",
                                message=f"Username: {information["email"]}\nPassword: {information["password"]}")
        else:
            messagebox.showinfo(title="Website not found", message=f"No details for the website {website} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(pady=50,padx=50)

canvas = tkinter.Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

label_website = tkinter.Label(text="Website:")
label_website.grid(column=0, row=1)
label_email = tkinter.Label(text="Email/Username:")
label_email.grid(column=0, row=2)
label_password = tkinter.Label(text="Password:")
label_password.grid(column=0, row=3)

entry_website = tkinter.Entry(width=32)
entry_website.grid(column=1, row=1, pady=5)
entry_website.focus()

entry_email = tkinter.Entry(width=32)
entry_email.grid(column=1, row=2,  pady=5)
entry_email.insert(0,"myemail@email.com")

entry_password = tkinter.Entry(width=32)
entry_password.grid(column=1, row=3, pady=5)

generate_button = tkinter.Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=47, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, pady=5)

search_button = tkinter.Button(text="Search", width=15, bg="light blue", fg="black", font=("arial",10,"normal"), highlightthickness=0, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()