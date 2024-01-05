import tkinter as tk
from tkinter import messagebox

class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Operations")

        # Initial balance
        self.balance = 1000

        # Label to display balance
        self.balance_label = tk.Label(root, text=f"Balance: ${self.balance}", font=('Arial', 14))
        self.balance_label.pack(pady=10)

        # Entry widget for amount
        self.amount_entry = tk.Entry(root, width=15, font=('Arial', 12))
        self.amount_entry.pack(pady=5)

        # Buttons
        tk.Button(root, text="Check Balance", command=self.check_balance).pack(pady=5)
        tk.Button(root, text="Deposit", command=self.deposit).pack(pady=5)
        tk.Button(root, text="Withdraw", command=self.withdraw).pack(pady=5)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your balance is ${self.balance}")

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount > 0:
                self.balance += amount
                self.update_balance_label()
            else:
                messagebox.showwarning("Invalid Amount", "Please enter a positive amount.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if 0 < amount <= self.balance:
                self.balance -= amount
                self.update_balance_label()
            else:
                messagebox.showwarning("Invalid Amount", "Insufficient funds or invalid amount.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    def update_balance_label(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
