import tkinter as tk
from tkinter import Toplevel
def open_new_window():
    new_window = Toplevel(root)
    new_window.geometry("200x100")
    new_window.title("Main")
    label = tk.Label(new_window, text="New window ")
    label.pack(pady=20)
root = tk.Tk()
root.geometry("300x200")
btn = tk.Button(root, text="Click here to open New Window", command=open_new_window)
btn.pack(pady=20)
root.mainloop()

