from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
#-----------------------------SEARCH FUNCTION------------------------------------#
def search():
    try:
        file = open("Password.json",mode="r")
        data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="ERROR!", message="No Passwords Registered")
    else:
        web = website_entry.get()
        if len(web)==0:
            messagebox.showerror(title=web, message="Please Fill The Entry")
        else:
            try:
                user = data[web]["Email"]
                pas = data[web]["Password"]
            except KeyError:
                messagebox.showerror(title=web, message="Not Found!")
            else:
                messagebox.showinfo(title=web, message=f"Username :{user}\nPassword : {pas}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters)  for _ in range(nr_letters)]
    password_list += ([random.choice(symbols) for _ in range(nr_symbols)])
    password_list += ([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(END, string=password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    password = password_entry.get()
    website = website_entry.get()
    email = email_entry.get()

    if len(password) == 0 or len(website) == 0:
        messagebox.showerror(title="Error!", message = "Some Field's Are Empty.\n\nPls Enter All the Details")
    else:
        is_ok = messagebox.askokcancel(title = "Conformation",
                                       message = f"Your Information Are :-\n\n"
                                                  f"Website : {website}\n"
                                                  f"Email : {email}\n"
                                                  f"Password : {password}"
                                       )
        new_data = {
            website:
            {
            "Email": email,
            "Password": password
            }
        }
        if is_ok:
            try:
                with open("Password.json",mode="r") as file:
                    temp = json.load(file)
                    temp.update(new_data)
            except FileNotFoundError:
                with open("Password.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("Password.json",mode="w") as file:
                    json.dump(temp,file,indent=4)
            finally:
                # clear's the entry in the window
                password_entry.delete(0, END)
                website_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50,pady=50)
window.title("PASSWORD MANAGER")

canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:",fg="Black")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:",fg="Black")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:",fg="Black")
password_label.grid(row=3,column=0)

website_entry = Entry(width=24)
website_entry.grid(row=1,column=1,columnspan=2,sticky="w")
website_entry.focus()

email_entry = Entry(width=44)
email_entry.insert(END,"shiwanshshukla25@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2,sticky="w")

password_entry = Entry(width=24)
password_entry.grid(row=3,column=1,sticky="w")

Generate_button = Button(text="Generate Password",width=15,command=generate)
Generate_button.grid(row=3,column=1,sticky="e",columnspan=2)

Search_button = Button(text="Search",width=15,command=search)
Search_button.grid(row=1,column=1,columnspan=2,sticky="e")

add_button = Button(text="ADD",width=37,command=add)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()