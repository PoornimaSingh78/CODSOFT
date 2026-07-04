import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password(length, include_letters, include_numbers, include_symbols):
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += "!@#$%^&*()-+"
    
    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = ''.join(secrets.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0.")
        return
    password=''.join(secrets.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    
    

root = tk.Tk()
root.title(" Random Password Generator")
root.geometry("800x600")
root.configure(bg="#E1EFC7")

tk.Label(root, text="Random Password Generator", font=("Helvetica", 22, "bold"), bg="#CDDBB2").pack(pady=19)

tk.Label(root, text=" Desired length of the password:", font=("Helvetica", 14 , "italic"), bg="#BFDE87").pack(pady=10)

length_entry = tk.Entry(root, font=("Helvetica", 15), width=10)
justify_center = tk.CENTER
length_entry.pack(pady=10)
length_entry.insert(0, "12")

options_frame = tk.Frame(root, bg="#B6EF4C")
options_frame.pack(pady=10)

letters=tk.BooleanVar(value=True)
numbers=tk.BooleanVar(value=True)
symbols=tk.BooleanVar(value=True)

tk.Checkbutton(options_frame, text="Include Letters", variable=letters, font=("Helvetica", 12), bg="#B6EF4C").pack(pady=5)
tk.Checkbutton(options_frame, text="Include Numbers", variable=numbers, font=("Helvetica", 12), bg="#B6EF4C").pack(pady=5)
tk.Checkbutton(options_frame, text="Include Symbols", variable=symbols, font=("Helvetica", 12), bg="#B6EF4C").pack(pady=5)

tk.Button(root, text="Generate Password", font=("Helvetica", 14), bg="#F0F7F0", command=lambda: generate_password(
    int(length_entry.get()),
    letters.get(),
    numbers.get(),
    symbols.get()
)).pack(pady=20)

password_entry = tk.Entry(root, font=("Helvetica", 17), width=30)
password_entry.pack(pady=10)
justify_center = tk.CENTER


root.mainloop()