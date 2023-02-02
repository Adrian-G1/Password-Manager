import tkinter as tk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
generate_button = tk.Button(text="Generate Password")
generate_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
