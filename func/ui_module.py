# ui_module.py

import tkinter as tk
from tkinter import ttk

def create_window(title, width, height):
    """
    Create a new tkinter window with the given title, width, and height.
    """
    window = tk.Tk()
    window.title(title)
    window.geometry(f"{width}x{height}")
    return window

def add_label(window, text, row, column):
    """
    Add a label to the window at the given row and column.
    """
    label = ttk.Label(window, text=text)
    label.grid(row=row, column=column)
    return label

def add_entry(window, row, column):
    """
    Add an entry field to the window at the given row and column.
    """
    entry = ttk.Entry(window)
    entry.grid(row=row, column=column)
    return entry

def add_button(window, text, command, row, column):
    """
    Add a button to the window at the given row and column.
    """
    button = ttk.Button(window, text=text, command=command)
    button.grid(row=row, column=column)
    return button

def add_separator(window, row, column, columnspan):
    """
    Add a separator to the window at the given row, column, and columnspan.
    """
    separator = ttk.Separator(window, orient=tk.HORIZONTAL)
    separator.grid(row=row, column=column, columnspan=columnspan, pady=2, padx=2)
    return separator

# Example usage
window = create_window("HyperMesh UI", 800, 600)

label_title = add_label(window, "HyperMesh", 0, 0)
label_username = add_label(window, "Username:", 1, 0)
entry_username = add_entry(window, 1, 1)
label_password = add_label(window, "Password:", 2, 0)
entry_password = add_entry(window, 2, 1)

def login():
    username = entry_username.get()
    password = entry_password.get()
    print(f"Username: {username}, Password: {password}")

button_login = add_button(window, "Login", login, 3, 0)
button_register = add_button(window, "Register", lambda: print("Register"), 3, 1)

add_separator(window, 4, 0, 2)

window.mainloop()
