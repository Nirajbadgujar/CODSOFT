import tkinter as tk
from tkinter import messagebox

def click_button(value):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current + str(value))

def clear_display():
    entry_display.delete(0, tk.END)

def calculate():
    try:
        expression = entry_display.get()
        result = str(eval(expression))
        entry_display.delete(0, tk.END)
        entry_display.insert(0, result)
    except:
        entry_display.delete(0, tk.END)
        entry_display.insert(0, "Error")


root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="White")


entry_display = tk.Entry(root, font=('Helvetica', 36), borderwidth=0, justify="right", bg="#34495e", fg="white")
entry_display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)


button_texts = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]


for text, row, col in button_texts:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=15, font=('Helvetica', 24), command=calculate, bg="#27ae60", fg="white", activebackground="#229954")
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=15, font=('Helvetica', 24), command=clear_display, bg="#e74c3c", fg="white", activebackground="white")
    else:
        button = tk.Button(root, text=text, padx=20, pady=15, font=('Helvetica', 24), command=lambda t=text: click_button(t), bg="#95a5a6", fg="white", activebackground="white")
    button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    root.grid_rowconfigure(row, weight=1)
    root.grid_columnconfigure(col, weight=1)


for widget in root.winfo_children():
    if isinstance(widget, tk.Button):
        widget.config(borderwidth=0, highlightthickness=0, relief="flat")


root.mainloop()
