from tkinter import*
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Warning there is a virus")
button = Button(root, text ="Virusscanner", command = msg)
button.place(x=50, y=80)
root.mainloop()
