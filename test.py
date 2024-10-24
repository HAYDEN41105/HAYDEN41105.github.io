import tkinter as tk
from tkinter import messagebox

class PizzaMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Maker")

        self.size_var = tk.StringVar(value="Medium")
        self.toppings_vars = {
            "Pepperoni": tk.BooleanVar(),
            "Mushrooms": tk.BooleanVar(),
            "Onions": tk.BooleanVar(),
            "Sausage": tk.BooleanVar(),
            "Bacon": tk.BooleanVar(),
            "Extra cheese": tk.BooleanVar(),
            "Black olives": tk.BooleanVar(),
            "Green peppers": tk.BooleanVar(),
            "Pineapple": tk.BooleanVar(),
            "Spinach": tk.BooleanVar()
        }

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Choose your pizza size:").pack(anchor=tk.W)
        sizes = ["Small", "Medium", "Large"]
        for size in sizes:
            tk.Radiobutton(self.root, text=size, variable=self.size_var, value=size).pack(anchor=tk.W)

        tk.Label(self.root, text="Choose your toppings:").pack(anchor=tk.W)
        for topping, var in self.toppings_vars.items():
            tk.Checkbutton(self.root, text=topping, variable=var).pack(anchor=tk.W)

        tk.Button(self.root, text="Make Pizza", command=self.make_pizza).pack()

    def make_pizza(self):
        size = self.size_var.get()
        toppings = [topping for topping, var in self.toppings_vars.items() if var.get()]
        toppings_str = ", ".join(toppings) if toppings else "no toppings"
        messagebox.showinfo("Pizza Order", f"You have ordered a {size} pizza with {toppings_str}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaMaker(root)
    root.mainloop()