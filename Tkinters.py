from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time

root = tk.Tk()
root.geometry ("500x500")

def showkey():
    messagebox.showwarning("A virus was detected", f"Our systems detected a computer virus in your system")


button = tk.Button(root, text="Scan for viruses", command=showkey)
button.place(x=250, y=250)


root.bind(button, showkey)
root.mainloop()