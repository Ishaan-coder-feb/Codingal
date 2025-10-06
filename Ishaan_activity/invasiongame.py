import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())

        simple_interest = (principal * rate * time) / 100

        compound_interest = principal * ((1 + rate / 100) ** time) - principal

        result_label.config(text=f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x300")
tk.Label(root, text="Principal Amount:").pack(pady=5)
principal_entry = tk.Entry(root)
principal_entry.pack()

tk.Label(root, text="Rate of Interest (% per annum):").pack(pady=5)
rate_entry = tk.Entry(root)
rate_entry.pack()

tk.Label(root, text="Time Period (years):").pack(pady=5)
time_entry = tk.Entry(root)
time_entry.pack()
calculate_button = tk.Button(root, text="Calculate", command=calculate_interest)
calculate_button.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()
root.mainloop()
