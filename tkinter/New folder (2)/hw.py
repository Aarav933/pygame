import tkinter as tk
from tkinter import messagebox
from datetime import date


def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birth_date = date(year, month, day)
        today = date.today()

        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Present Age: {age} years")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Age Calculator App")
root.geometry("450x300")
root.config(bg="white")
title_label = tk.Label(
    root,
    text="Age Calculator App",
    font=("Arial", 22, "bold"),
    bg="white",
    fg="black"
)
title_label.pack(pady=15)

subtitle_label = tk.Label(
    root,
    text="Tkinter Geometry Managers",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="gray"
)
subtitle_label.pack(pady=5)

instruction_label = tk.Label(
    root,
    text="Enter your date of birth",
    font=("Arial", 12),
    bg="white",
    fg="black"
)
instruction_label.pack(pady=10)
input_frame = tk.Frame(root, bg="white")
input_frame.pack(pady=10)
tk.Label(input_frame, text="Day", font=("Arial", 11), bg="white").grid(row=0, column=0, padx=10, pady=5)
day_entry = tk.Entry(input_frame, width=8, font=("Arial", 11))
day_entry.grid(row=1, column=0, padx=10)
tk.Label(input_frame, text="Month", font=("Arial", 11), bg="white").grid(row=0, column=1, padx=10, pady=5)
month_entry = tk.Entry(input_frame, width=8, font=("Arial", 11))
month_entry.grid(row=1, column=1, padx=10)
tk.Label(input_frame, text="Year", font=("Arial", 11), bg="white").grid(row=0, column=2, padx=10, pady=5)
year_entry = tk.Entry(input_frame, width=10, font=("Arial", 11))
year_entry.grid(row=1, column=2, padx=10)
calc_button = tk.Button(
    root,
    text="Calculate Age",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    command=calculate_age
)
calc_button.pack(pady=20)

result_label = tk.Label(
    root,
    text="Present Age: ",
    font=("Arial", 13, "bold"),
    bg="white",
    fg="blue"
)
result_label.pack(pady=10)

root.mainloop()
