import tkinter as tk
from tkinter import messagebox
def calculateproduct():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1*num2
        result_label.config(text=f"product: {product}")
    except:
        messagebox.showerror("Error", "Enter number please")
window = tk.Tk()
window.title("Product Calculator")
window.geometry("400x200")
tk.Label(window, text="1. number").pack()
entry1  = tk.Entry(window)
entry1.pack()
tk.Label(window, text="2. number").pack()
entry2  = tk.Entry(window)
entry2.pack()
tk.Button(window, text="Product", command = calculateproduct).pack()
result_label = tk.Label(window, text="Product:")
result_label.pack()

window.mainloop()


