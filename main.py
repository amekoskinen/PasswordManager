import tkinter
from tkinter import PhotoImage, END, messagebox
import random
import pyperclip
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
    if password == "" or website =="":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the information you entered\nEmail: {email} and password:{password}\nDo you want to save the information?")
        if is_ok:
            add_text=f"{website} | {email} | {password}\n"
            with open("data.txt","a") as pwd_file:
                pwd_file.write(add_text)
            entry_website.delete(0,END)
            entry_password.delete(0,END)


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

entry_website = tkinter.Entry(width=45)
entry_website.grid(column=1, row=1, columnspan=2, pady=5)
entry_website.focus()

entry_email = tkinter.Entry(width=45)
entry_email.grid(column=1, row=2, columnspan=2, pady=5)
entry_email.insert(0,"myemail@email.com")

entry_password = tkinter.Entry(width=26)
entry_password.grid(column=1, row=3, pady=5)

generate_button = tkinter.Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=40, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, pady=5)



window.mainloop()