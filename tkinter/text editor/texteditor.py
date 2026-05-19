from tkinter import*
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = Tk()
window.title("Text Editor")
window.geometry("200x200")
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
filepath = None
def newfile():
    global filepath
    filepath = None
    txt_edit.delete(1.0, END)
    window.title("New file")
def openfile():
    global filepath
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END) 
    with open(filepath, "r") as file:
        txt_edit.insert(END, file.read())
    window.title(f"opened - {filepath}")
def savefile():
    global filepath
    if filepath:
        with open(filepath, "w") as file:
            file.write(txt_edit.get(1.0, END))
    else:
        saveas()
def saveas():
    global filepath 
    filepath = askopenfilename(
        defaultextension=".txt", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if not filepath:
        return  
    with open(filepath, "w") as file:
            file.write(txt_edit.get(1.0, END))
    window.title(f"saved - {filepath}")
def updatestatus(event=None):
    row, col = txt_edit.index(INSERT).split(".")
    status_bar.config(text=f"Line: {row} Column:{col}")
frame = Frame(window)

frame.grid(row=0, column=0, sticky="nsew")

scroll = Scrollbar(frame)

scroll.pack(side=RIGHT, fill=Y)

txt_edit = Text(frame, undo=True, yscrollcommand=scroll.set)

txt_edit.pack(expand=True, fill="both")

scroll.config(command=txt_edit.yview)

# Status Bar

status_bar = Label(window, text="Line: 1 | Column: 0", anchor="e")

status_bar.grid(row=1, column=0, sticky="ew")

txt_edit.bind("<KeyRelease>", updatestatus)
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=newfile, accelerator="Ctrl+N")
filemenu.add_command(label="Open", command=openfile, accelerator="Ctrl+O")
filemenu.add_command(label="save", command=savefile, accelerator="Ctrl+S")
filemenu.add_command(label="save as", command=saveas)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
edit_menu = Menu(menu, tearoff=0)

menu.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Undo", command=txt_edit.edit_undo, accelerator="Ctrl+Z")

edit_menu.add_command(label="Redo", command=txt_edit.edit_redo, accelerator="Ctrl+Y")

edit_menu.add_separator()

edit_menu.add_command(label="Cut", command=lambda: txt_edit.event_generate("<<Cut>>"))

edit_menu.add_command(label="Copy", command=lambda: txt_edit.event_generate("<<Copy>>"))

edit_menu.add_command(label="Paste", command=lambda: txt_edit.event_generate("<<Paste>>"))
window.bind("<Control-n>", lambda e: newfile())

window.bind("<Control-o>", lambda e: openfile())

window.bind("<Control-s>", lambda e: savefile())

window.bind("<KeyRelease>", updatestatus)

# Run App

window.mainloop()
