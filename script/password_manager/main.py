from tkinter import * ## this import only class and constants
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list =password_letter + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry_box.insert(0,password)
    pyperclip.copy(password) 

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry_box.get()
    email = email_entry_box.get()
    password = password_entry_box.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
      messagebox.showerror("Error","Please fill all fields")
    else:
        confirm = messagebox.askokcancel(title="confirm", message="Are you sure you want to save this password?")
        if confirm:
            with open("data_file.txt", "a") as data_file:
                data_file.write(f" {website} | {email} | {password}\n")
                website_entry_box.delete(0, END)
                password_entry_box.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

lock_image=PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=190,highlightthickness=0)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entry

website_entry_box = Entry(width=40)
website_entry_box.grid(row=1, column=1,columnspan=2)
website_entry_box.focus()
email_entry_box = Entry(width=40)
email_entry_box.grid(row=2, column=1,columnspan=2)
email_entry_box.insert(0,"akanksha.borkar4@gmail.com")
password_entry_box = Entry(width=20,highlightthickness=0)
password_entry_box.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password",width=15,highlightthickness=0,command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button=Button(text="Add",width=30,command=save)
add_button.grid(row=4, column=1,columnspan=2)

window.mainloop()
