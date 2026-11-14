from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("500x500")
def handle_keypress(event):
    """print the character associated with a key press"""
    print(event.char)
window.bind("<KeyPress>", handle_keypress)
def handle_click(event):
    """print the mouse button pressed"""
    print("the buttonwas clicked!")
btn = Button(window, text="Click Me")
btn.pack()
btn.bind("<Button-1>", handle_click)
window.mainloop()