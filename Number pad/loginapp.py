from tkinter import *
root = Tk()
root.title('Login App')
root.geometry('200x400')
frame = Frame(master=root , height =200, width=300,bg='blue' )
lbl1 = Label(frame,text="Name:", bg="yellow", fg="green", width = 12)
lbl2 = Label(frame,text="Email:", bg="yellow", fg="green", width = 12)
lbl3 = Label(frame,text="Password:", bg="yellow", fg="green", width = 12)
name_entry=Entry(frame)
email_entry=Entry(frame)
password_entry=Entry(frame)
def display():
    name = name_entry.get()
    hello = 'Hello'+name
    message = "Congrataulations!!!"
    textbox.insert(END, hello)
    textbox.insert(END, message)
textbox  = Text(bg="white", fg="black")
