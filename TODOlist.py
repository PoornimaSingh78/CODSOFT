import os
import tkinter as tk
from tkinter import ttk , messagebox
import json

class ModernTodo:
    def __init__(self, master):
        self.master = master
        
        self.master.title("Modern To-Do List")
        self.master.geometry("600x800")
        self.master.resizable(False, False)

        style  = ttk.Style()
        style.theme_use('clam')

        style.configure('TButton', font=('Helvetica', 10), padding=10, foreground='white', background='green')
        style.configure('Tframe', background="#2559db")
        style.configure('TEntry', font=('Helvetica', 10), padding=10)
        style.configure('Treeview', font=('Helvetica', 10), padding=10)
        style.configure('Treeview.Heading', font=('Helvetica', 10, 'bold'), padding=10)
        self.frame = ttk.Frame(self.master, padding=10)
        self.frame.pack(fill=tk.BOTH, expand=True)


        self.task_var = tk.StringVar()
        self.task_entry = ttk.Entry(self.frame, textvariable=self.task_var, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, pady=10, sticky='ew')

        self.add_button = ttk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10, sticky='ew')

        self.task_tree = ttk.Treeview(self.frame, columns=("Task"), show='headings', height=18)
        self.task_tree.heading("Task", text="Task")
        self.task_tree.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')

        scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.task_tree.yview)
        scrollbar.grid(row=1, column=2, sticky='ns')
        self.task_tree.configure(yscrollcommand=scrollbar.set)

        self.delete_button = ttk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=5, pady=10, sticky='ew')

        self.__save_button = ttk.Button(self.frame, text="Save Tasks", command=self.save_tasks)
        self.__save_button.grid(row=2, column=1, padx=5, pady=10, sticky='ew')

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.load_tasks()

       



    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.task_tree.insert('', 'end', values=(task,))
            self.task_var.set('')
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected = self.task_tree.selection()
        if selected:
            for item in selected:
                self.task_tree.delete(item)
        else:
            messagebox.showwarning("Warning", "Please choose a task.")

    def save_tasks(self):
        tasks = [self.task_tree.item(item, 'values')[0] for item in self.task_tree.get_children()]
        try:
            with open('tasks.json', 'w') as f:
                json.dump(tasks, f)
            messagebox.showinfo("Info", "Tasks saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks: {e}")

    def load_tasks(self):
        if os.path.exists('tasks.json'):
            try:
                with open('tasks.json', 'r') as f:
                    tasks = json.load(f)
                for task in tasks:
                    self.task_tree.insert('', tk.END, values=(task,))
            except FileNotFoundError:
                pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernTodo(root)
    root.mainloop()

