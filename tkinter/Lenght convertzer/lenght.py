import tkinter as tk
from tkinter import messagebox

def convert_to_cm():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("300x150")
label = tk.Label(root, text="Enter length in inches:")
label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)
convert_button = tk.Button(root, text="Convert", command=convert_to_cm)
convert_button.pack(pady=5)
result_label = tk.Label(root, text="Result will appear here")
result_label.pack(pady=5)
root.mainloop()