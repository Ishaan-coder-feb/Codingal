import tkinter as tk
from tkinter import messagebox
import random

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

def determine_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x200")
title_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 12))
title_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()
button_frame=tk,root()

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play("Rock"), width=10)
paper_button = tk.Button(button_frame, text="Paper", command=lambda: play("Paper"), width=10)
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play("Scissors"), width=10)

rock_button.grid(row=0, column=0, padx=5, pady=5)
paper_button.grid(row=0, column=1, padx=5, pady=5)
scissors_button.grid(row=0, column=2, padx=5, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10 ,pady=12)


root.mainloop()
