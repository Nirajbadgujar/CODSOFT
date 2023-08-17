import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400") 
        self.root.configure(bg="White")  
        
        self.label_title = tk.Label(root, text="Random Password Generator", font=("Helvetica", 20, "bold"), bg="White")
        self.label_title.pack(pady=10)

        self.label_length = tk.Label(root, text="Password Length:", font=("Helvetica", 12), bg="White")
        self.label_length.pack(pady=(20, 5))

        self.length_entry = tk.Entry(root, font=("Helvetica", 12))
        self.length_entry.pack(pady=5)

        self.uppercase_var = tk.IntVar()
        self.lowercase_var = tk.IntVar()
        self.numbers_var = tk.IntVar()
        self.special_var = tk.IntVar()

        self.uppercase_checkbox = tk.Checkbutton(root, text="Uppercase", variable=self.uppercase_var,
                                                font=("Helvetica", 12), bg="White", padx=10)
        self.lowercase_checkbox = tk.Checkbutton(root, text="Lowercase", variable=self.lowercase_var,
                                                font=("Helvetica", 12), bg="White", padx=10)
        self.numbers_checkbox = tk.Checkbutton(root, text="Numbers", variable=self.numbers_var,
                                              font=("Helvetica", 12), bg="White", padx=10)
        self.special_checkbox = tk.Checkbutton(root, text="Special characters", variable=self.special_var,
                                               font=("Helvetica", 12), bg="White", padx=10)

        self.uppercase_checkbox.pack(anchor="w")
        self.lowercase_checkbox.pack(anchor="w")
        self.numbers_checkbox.pack(anchor="w")
        self.special_checkbox.pack(anchor="w")

        self.generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12),
                                         command=self.generate_password, bg="#4CAF50", fg="white")
        self.generate_button.pack(pady=20)

        self.generated_password_label = tk.Label(root, text="", font=("Helvetica", 14), bg="White")
        self.generated_password_label.pack(pady=10)

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
            
            if password_length <= 0:
                messagebox.showerror("Invalid Input", "Password length should be a positive integer.")
                return
            
            allowed_characters = ""
            if self.uppercase_var.get():
                allowed_characters += string.ascii_uppercase
            if self.lowercase_var.get():
                allowed_characters += string.ascii_lowercase
            if self.numbers_var.get():
                allowed_characters += string.digits
            if self.special_var.get():
                allowed_characters += string.punctuation
            
            if not allowed_characters:
                messagebox.showerror("Invalid Input", "Select at least one complexity option.")
                return
            
            password = self.generate_password_string(password_length, allowed_characters)
            self.generated_password_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive integer for password length.")
    
    def generate_password_string(self, length, allowed_characters):
        password = ''.join(random.choice(allowed_characters) for _ in range(length))
        password = ''.join(random.sample(password, len(password))) 
        return password

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
