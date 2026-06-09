from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time

root = tk.Tk()
root.geometry ("500x500")

def showkey(event):
    messagebox.showinfo("Key press detected", f"Our systems detected you pressed the key {event.keysym}")


root.bind("<Key>", showkey)

root.mainloop()