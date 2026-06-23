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
            quantityentry = ttk.Entry(frame, width=2)
            quantityentry.grid(row=1, column=1, padx=5,pady=5)
            self.menu_quantity[item]=quantityentry
        self.currencyvar = tk.StringVar()
        ttk.Label(
            frame, text="Currency", font=("Arial", 12)
        ).grid(
            row=len(self.menu) + 1,
            column = 0, padx = 10, pady=10
        )
        currencydropdown =ttk.Combobox(frame, textvariable=self.currencyvar, state="readonly", width=15, values=("USD", "EUR"))
        currencydropdown.grid(row=len(self.menu, column=1, padx=10, pady=10))
        currencydropdown.cuurent(0)
        self.currencyvar.trace("w", self.cost)
        orderbutton = ttk.Button(frame, text="Place order", command= self.placeorder)
        orderbutton.grid(row=len(self.menu)+2, columnspan=3, padx=10,pady=10)
