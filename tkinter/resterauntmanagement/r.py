import tkinter as tk
from tkinter import ttk, messagebox

class resterauntorders:
    def __init__(self, root):
        self.root = root
        self.root.title("Resteraunt Order App")
        self.menu = {"Fries": 2, 
                     "Burger": 2,
                     "Pizza": 3, 
                     "Drinks": 1,
                     "Pancakes": 4}
        self.exangerate = 82
        self.setup_background(root)
        frame = ttk.Frame(root)
        frame.place(relx = 1, rely = 1, anchor=tk.CENTER)
        ttk.Label(
            frame, text="resteraunt orders ", font=("Arial", 20,"bold")
        ).grid(row=0,columnspan=5, padx = 20, pady=20 )
        self.menu_labels={}
        self.menu_quantity={}
        for i, (item , cost) in enumerate(self.menu.items(), start=1):
            label = ttk.Label(frame, text="{item}" "{cost}"), font=("Arial", 12)
        label.grid(row=i, column =0, padx = 20, pady = 20)
        self.menu_labels[item] = label