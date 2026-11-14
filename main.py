from tkinter import Tk, Label, Button
from tkinter import messagebox

root = Tk()
root.title("Routine Checker")
root.geometry("400x400")
root.resizable(False, False)

lbl = Label(root, text="Routine Check", font=("Arial", 40), fg="white", bg="black")
lbl.pack(pady=20)

lbl1 = Label(root, text="HAVE YOU DONE YOUR TASKS?", font=("Arial", 14))
lbl1.pack(pady=10)

lbl2 = Label(root, text="", font=("Arial", 14), fg="green")
lbl2.pack(pady=10)


def no():
    messagebox.showinfo("Routine Check", "Please complete your tasks before proceeding.")


def yes():
    messagebox.showinfo("Routine Check", "Great job! Keep up the good work.")
    lbl2.config(text="You have completed your tasks!")


btn = Button(root, text="Yes", command=yes, width=10, height=2)
btn.place(x=100, y=220)
            
btn1 = Button(root, text="No", command=no, width=10, height=2)
btn1.place(x=220, y=220)

root.mainloop()