from tkinter import*
from datetime import date
window = Tk()
window.title("Screen")
window.geometry("400x200")
lbl = Label(text="Hey There!", fg="white", bg="blue", height=1, width=400)
namelbl = Label(text="Name", bg="green")
nameentry = Entry()
def display():
    name = nameentry.get()
    global Message
    Message = "Welcome todays date is:"
    hello = "Hello"+name
    text_box.insert(END , hello)
    text_box.insert(END , Message)
    text_box.insert(END, date.today())
text_box = Text(height = 1)
button = Button(text ="Start", command=display, height = 1, bg="yellow", fg="red")
lbl.pack()
namelbl.pack()
nameentry.pack()
button.pack()
text_box.pack()
window.mainloop()