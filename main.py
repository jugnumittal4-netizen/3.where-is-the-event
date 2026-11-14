from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("400x400")
def msg():
    messagebox.showwarning("Virus Detected", "A virus has been detected on your system. Please take immediate action to remove it.")
btn = Button(root, text="Check for Virus", command=msg)
btn.place(x=150, y=180)
root.mainloop()