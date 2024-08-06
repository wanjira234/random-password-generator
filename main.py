import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import sqlite3


# password creation


def generate_password():
    try:
        total_length = int(length_entry.get())
        num_uppercase = int(uppercase_entry.get())
        num_lowercase = int(lowercase_entry.get())
        num_numbers = int(numbers_entry.get())
        num_special = int(special_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
        return

    if num_uppercase + num_lowercase + num_numbers + num_special > total_length:
        messagebox.showerror("Error", "Sum of individual character types exceeds total length")
        return

    password_chars = []
    password_chars.extend(random.choices(string.ascii_uppercase, k=num_uppercase))
    password_chars.extend(random.choices(string.ascii_lowercase, k=num_lowercase))
    password_chars.extend(random.choices(string.digits, k=num_numbers))
    password_chars.extend(random.choices(string.punctuation, k=num_special))

    remaining_length = total_length - len(password_chars)
    if remaining_length > 0:
        all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        password_chars.extend(random.choices(all_chars, k=remaining_length))

    random.shuffle(password_chars)
    password = ''.join(password_chars)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# les save in a db


def save_password():
    site = site_entry.get()
    password = password_entry.get()
    if site and password:
        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO passwords (site, password) VALUES (?, ?)', (site, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Password saved to database")
        display_saved_passwords()
    else:
        messagebox.showerror("Error", "Site and password must be provided")


# allow for copies to be made


def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard")
    else:
        messagebox.showerror("Error", "No password to copy")


#  lets' store the password


def create_database():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            site TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# lets' display password history and site


def display_saved_passwords():
    for row in tree.get_children():
        tree.delete(row)
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('SELECT site, password FROM passwords')
    for row in cursor.fetchall():
        tree.insert('', 'end', values=row)
    conn.close()


# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create and place the widgets
tk.Label(root, text="Site:").grid(row=0, column=0, sticky='e')
site_entry = tk.Entry(root)
site_entry.grid(row=0, column=1)

tk.Label(root, text="Password Length:").grid(row=1, column=0, sticky='e')
length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1)
length_entry.insert(0, "12")

tk.Label(root, text="Uppercase Letters:").grid(row=2, column=0, sticky='e')
uppercase_entry = tk.Entry(root)
uppercase_entry.grid(row=2, column=1)
uppercase_entry.insert(0, "2")

tk.Label(root, text="Lowercase Letters:").grid(row=3, column=0, sticky='e')
lowercase_entry = tk.Entry(root)
lowercase_entry.grid(row=3, column=1)
lowercase_entry.insert(0, "2")

tk.Label(root, text="Numbers:").grid(row=4, column=0, sticky='e')
numbers_entry = tk.Entry(root)
numbers_entry.grid(row=4, column=1)
numbers_entry.insert(0, "2")

tk.Label(root, text="Special Characters:").grid(row=5, column=0, sticky='e')
special_entry = tk.Entry(root)
special_entry.grid(row=5, column=1)
special_entry.insert(0, "2")

tk.Button(root, text="Generate Password", command=generate_password).grid(row=6, column=0, columnspan=2)

tk.Label(root, text="Generated Password:").grid(row=7, column=0, sticky='e')
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=7, column=1)

tk.Button(root, text="Save to Database", command=save_password).grid(row=8, column=0, columnspan=2)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=9, column=0, columnspan=2)

# Treeview to display saved passwords
columns = ('site', 'password')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('site', text='Site')
tree.heading('password', text='Password')
tree.grid(row=10, column=0, columnspan=2)

# Initialize the database and display saved passwords
create_database()
display_saved_passwords()

# Start the main event loop
root.mainloop()
