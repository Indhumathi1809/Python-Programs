import tkinter as tk
from datetime import datetime

class AgeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator")

        # Entry widgets for birthdate
        self.birthdate_label = tk.Label(root, text="Enter Birthdate (YYYY-MM-DD):", font=('Arial', 12))
        self.birthdate_label.pack(pady=10)

        self.birthdate_entry = tk.Entry(root, width=15, font=('Arial', 12))
        self.birthdate_entry.pack(pady=10)

        # Button to calculate age
        tk.Button(root, text="Calculate Age", command=self.calculate_age).pack(pady=10)

        # Label to display age
        self.age_label = tk.Label(root, text="", font=('Arial', 14))
        self.age_label.pack(pady=10)

    def calculate_age(self):
        birthdate_str = self.birthdate_entry.get()
        
        try:
            birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
            today = datetime.now()
            
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            
            self.age_label.config(text=f"Your age is {age} years.")
        except ValueError:
            self.age_label.config(text="Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalculator(root)
    root.mainloop()
