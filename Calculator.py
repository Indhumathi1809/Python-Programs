import tkinter as tk

def button_click(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(symbol))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry widget for displaying the expression
entry = tk.Entry(window, width=20, font=('Arial', 16), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 14),
              command=lambda b=button: button_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(window, text='C', padx=20, pady=20, font=('Arial', 14), command=clear_entry).grid(row=row_val, column=col_val)

# Run the main loop
window.mainloop()
