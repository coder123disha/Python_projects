import tkinter as tk
from tkinter import messagebox, simpledialog

# Global list to store tasks
todo_list = []

# Functions
def add_task():
    task = task_entry.get().strip()
    if task:
        todo_list.append({"Task": task, "Status": "Pending"})
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(todo_list, start=1):
        task_listbox.insert(tk.END, f"{idx}. {task['Task']} - {task['Status']}")

def remove_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        removed_task = todo_list.pop(index)
        update_listbox()
        messagebox.showinfo("Task Removed", f"Removed: {removed_task['Task']}")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def mark_completed():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        todo_list[index]['Status'] = "Done!!"
        update_listbox()
        messagebox.showinfo("Task Completed", f"Task marked as completed: {todo_list[index]['Task']}")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("450x500")
root.config(bg="#f4f4f4")

title = tk.Label(root, text="To-Do List with Status", font=("Helvetica", 18, "bold"), bg="#f4f4f4")
title.pack(pady=10)

task_entry = tk.Entry(root, width=30, font=("Helvetica", 14))
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task, width=20, bg="#90ee90", font=("Helvetica", 12))
add_btn.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10, font=("Helvetica", 12), selectbackground="#dcdcdc")
task_listbox.pack(pady=10)

mark_btn = tk.Button(root, text="Mark as Completed", command=mark_completed, width=20, bg="#87ceeb", font=("Helvetica", 12))
mark_btn.pack(pady=5)

remove_btn = tk.Button(root, text="Remove Task", command=remove_task, width=20, bg="#ff6961", font=("Helvetica", 12))
remove_btn.pack(pady=5)

# Run the GUI loop
root.mainloop()
