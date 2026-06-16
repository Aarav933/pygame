from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.geometry("700x700")
root.title("denomination Calculator")
root.configure(bg="blue")
upload = Image.open("app_img.jpg")
upload = upload.resize((200,200))
image = ImageTk.PhotoImage(upload)
l = Label(root, text="welcome", bg="blue", image=image)
l.place(x=150, y=50)
label1 = Label(root, bg="light blue")
label1.place(relx=0.5, y=200, anchor=CENTER)
def msg():
    MsgBox = messagebox.showinfo("Do oyou want to calculate the denomination count?")
    if MsgBox=="ok":
        topwin()
button = Button(root, text="Get started", bg="black", fg="white")
button.place(x=200, y=20)
def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.geometry("400x400")
    top.configure(bg="light blue")
    label = Label(root, text="Enter note count", bg="grey")
    l1 = Label(top, text="2000", bg="grey")
    l2 = Label(top, text="500", bg="grey")
    l3 = Label(top, text="100", bg="grey")