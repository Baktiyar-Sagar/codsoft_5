import tkinter as tk
from tkinter import messagebox

def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(value))

def clear_entry():
    entry_var.set("")

def delete_last():
    current_text = entry_var.get()
    entry_var.set(current_text[:-1])

def calculate():
    try:
        expression = entry_var.get()
        result = eval(expression)
        entry_var.set(result)
    except Exception:
        messagebox.showerror("Error", "Invalid expression!")
        entry_var.set("")

# GUI Setup
root = tk.Tk()
root.title("Simple Calculator")
entry_var = tk.StringVar()

tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify='right', bd=10, relief=tk.GROOVE).grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    action = lambda x=text: on_button_click(x) if x != '=' else calculate()
    tk.Button(root, text=text, font=("Arial", 20), command=action, width=5, height=2).grid(row=row, column=col)

tk.Button(root, text="C", font=("Arial", 20), command=clear_entry, width=5, height=2).grid(row=5, column=0, columnspan=2)
tk.Button(root, text="DEL", font=("Arial", 20), command=delete_last, width=5, height=2).grid(row=5, column=2, columnspan=2)

root.mainloop()
