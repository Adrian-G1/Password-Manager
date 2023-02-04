import tkinter as tk
import json as js
from tkinter import messagebox
from generator import generate_password


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password():
    password = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) or len(password):
        try:
            with open("data.json", "r") as file:
                # Read old data
                data = js.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Saving data
                js.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving data
                js.dump(new_data, file, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            website_entry.focus()
    else:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry(width=38)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = tk.Entry(width=38)
email_entry.insert(0, "agarcia00515@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = tk.Button(text="Generate Password", command=random_password)
generate_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
