import tkinter as tk
from tkinter import messagebox


def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error")
                return
            result = num1 / num2
            
        
        label_result.config(text=f"Result: {result}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")


def clear_all():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ")


root = tk.Tk()
root.title("Two-Number Math Calculator")
root.geometry("680x500")
root.config(bg="#D896E4")


font_style = ("Helvetica", 14)
button_style = {"font": ("Helvetica", 12, "bold"), "fg": "white", "bg": "#6e0378", "activebackground": "#98a5a3", "borderwidth": 0, "padx": 10, "pady": 10}

#input1
tk.Label(root, text="Enter First Number:", bg="#8b7d91", fg="black", font=font_style).pack(pady=(20, 5))
entry_num1 = tk.Entry(root, font=font_style, width=20, justify="center")
entry_num1.pack(pady=5)

# input2
tk.Label(root, text="Enter Second Number:", bg="#8b7d91", fg="black", font=font_style).pack(pady=(15, 5))
entry_num2 = tk.Entry(root, font=font_style, width=20, justify="center")
entry_num2.pack(pady=5)


tk.Label(root, text="Choose Operation", bg="#bdaded", fg="#161717", font=("Helvetica", 15)).pack(pady=(15, 10))

frame_buttons = tk.Frame(root, bg="#2c3e50")
frame_buttons.pack()

add_button = tk.Button(frame_buttons, text=" + ", command=lambda: calculate("+"), **button_style)
add_button.grid(row=0, column=0, padx=5, pady=5)

subtract_button = tk.Button(frame_buttons, text=" - ", command=lambda: calculate("-"), **button_style)
subtract_button.grid(row=0, column=1, padx=5, pady=5)

multiply_button = tk.Button(frame_buttons, text=" * ", command=lambda: calculate("*"), **button_style)
multiply_button.grid(row=0, column=2, padx=5, pady=5)

division_button = tk.Button(frame_buttons, text=" / ", command=lambda: calculate("/"), **button_style)
division_button.grid(row=0, column=3, padx=5, pady=5)


label_result = tk.Label(root, text="Result: ", bg="#5c7083", fg="#A056BD", font=("Helvetica", 16, "bold"), width=25, height=2, relief="sunken")
label_result.pack(pady=20)

clear_button = tk.Button(root, text="Clear All", command=clear_all, font=("Helvetica", 11, "bold"), bg="#cb1f0c", fg="white", activebackground="#c0392b", padx=10, pady=5)
clear_button.pack()

root.mainloop()

