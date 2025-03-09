import tkinter as tk
import random


def play(choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)

    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == 'Rock' and computer_choice == 'Scissors') or \
            (choice == 'Scissors' and computer_choice == 'Paper') or \
            (choice == 'Paper' and computer_choice == 'Rock'):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=f"You: {choice} | Computer: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x200")

tk.Label(root, text="Choose Rock, Paper, or Scissors:").pack()

buttons_frame = tk.Frame(root)
buttons_frame.pack()

tk.Button(buttons_frame, text="Rock", command=lambda: play("Rock"), width=10).grid(row=0, column=0)
tk.Button(buttons_frame, text="Paper", command=lambda: play("Paper"), width=10).grid(row=0, column=1)
tk.Button(buttons_frame, text="Scissors", command=lambda: play("Scissors"), width=10).grid(row=0, column=2)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
