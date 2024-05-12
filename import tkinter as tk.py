import tkinter as tk
from tkinter import messagebox

class Menu:
    def __init__(self):
        self.items = {
            'Category1': {'Item1': 350, 'Item2': 350, 'Item3': 350},
            'Category2': {'Item4': 1100, 'Item5': 400, 'Item6': 400},
            'Category3': {'Item7': 350, 'Item8': 300, 'Item9': 150},
            'Category4': {'Item10': 100, 'Item11': 100, 'Item12': 100},
            'Category5': {'Item13': 200, 'Item14': 150, 'Item15': 350}
        }

class OrderSystem:
    def __init__(self, menu):
        self.menu = menu
        self.order_vars = {}
        self.menu_item_price = {}

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("Order System")
        self.root.geometry("800x600")

        for category, items in self.menu.items.items():
            category_label = tk.Label(self.root, text=category.capitalize(), font=("Arial", 16, "bold"))
            category_label.pack()

            for item, price in items.items():
                item_frame = tk.Frame(self.root)
                item_frame.pack(anchor="w")

                item_label = tk.Label(item_frame, text=f"{item} - ₦{price}", font=("Arial", 12))
                item_label.pack(side="left")

                self.order_vars[item] = tk.IntVar()
                item_entry = tk.Entry(item_frame, textvariable=self.order_vars[item], width=5)
                item_entry.pack(side="left")

                self.menu_item_price[item] = price

        self.total_label = tk.Label(self.root, text="", font=("Helvetica", 14, "bold"))
        self.total_label.pack()

        submit_button = tk.Button(self.root, text="Submit Order", command=self.calculate_total, bg="green", fg="white")
        submit_button.pack()

    def calculate_total(self):
        total = sum(self.menu_item_price[item] * quantity.get() for item, quantity in self.order_vars.items())

        discount = 0
        if total >= 3000 and total < 5000:
            discount = 0.1
        elif total >= 5000 and total < 10000:
            discount = 0.15
        elif total >= 10000:
            discount = 0.25

        total_charge = total * (1 - discount)
        total_charge_str = f"Total Charges: ₦{int(total_charge)}"
        self.total_label.config(text=total_charge_str)

    def run(self):
        self.create_gui()
        self.root.mainloop()

if __name__ == "__main__":
    menu = Menu()
    order_system = OrderSystem(menu)
    order_system.run()