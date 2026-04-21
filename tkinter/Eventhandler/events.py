from tkinter import*
window = Tk()
window.title("Events")
window.geometry("200x200")
def handle_keypress(event):
    print(event.char)
window.bind("<Key>", handle_keypress)
def handle_click(event):
    print("You clicked the button")
button = Button(text="click me")
button.pack()
window.bind("<Button>", handle_click)
window.mainloop()