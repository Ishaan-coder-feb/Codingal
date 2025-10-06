import tkinter as tk
def check_password_strength():
    password = entry_password.get()
    length = len(password)
    
    if length <= 5:
        strength.set("Weak")
        label_strength.config(fg="red")
    elif 6 <= length <= 8:
        strength.set("Medium")
        label_strength.config(fg="black")
    elif 9 <= length <= 12:
        strength.set("Strong")
        label_strength.config(fg="light green")
    else:
        strength.set("Very Strong")
        label_strength.config(fg="dark green")
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
label_instruction = tk.Label(root, text="Enter Password:")
label_instruction.pack(pady=10)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack(pady=5)
button_check = tk.Button(root, text="Check Strength", command=check_password_strength)
button_check.pack(pady=10)
strength = tk.StringVar()
label_strength = tk.Label(root, textvariable=strength, font=("Arial", 12, "bold"))
label_strength.pack(pady=10)
root.mainloop()
