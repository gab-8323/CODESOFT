import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = 'Completed' if self.completed else 'Not Completed'
        return f"{self.title} - {self.description} [{status}]"

tasks = []

def add_task():
    title = entry_title.get()
    description = entry_description.get()
    if title and description:
        task = Task(title, description)
        tasks.append(task)
        listbox_tasks.insert(tk.END, task.title)
        entry_title.delete(0, tk.END)
        entry_description.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both title and description")

def view_task(event):
    index = listbox_tasks.curselection()[0]
    task = tasks[index]
    messagebox.showinfo("Task Details", str(task))

def delete_task():
    index = listbox_tasks.curselection()[0]
    tasks.pop(index)
    listbox_tasks.delete(index)

def mark_task_completed():
    index = listbox_tasks.curselection()[0]
    tasks[index].mark_completed()
    listbox_tasks.delete(index)
    listbox_tasks.insert(index, tasks[index].title)

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry_title = tk.Entry(frame, width=30)
entry_title.pack(side=tk.LEFT, padx=5)
entry_title.insert(0, "Task Title")

entry_description = tk.Entry(frame, width=30)
entry_description.pack(side=tk.LEFT, padx=5)
entry_description.insert(0, "Task Description")

btn_add = tk.Button(frame, text="Add Task", command=add_task)
btn_add.pack(side=tk.LEFT, padx=5)

listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)
listbox_tasks.bind('<Double-1>', view_task)

btn_delete = tk.Button(root, text="Delete Task", command=delete_task)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_mark_completed = tk.Button(root, text="Mark Completed", command=mark_task_completed)
btn_mark_completed.pack(side=tk.LEFT, padx=5)

root.mainloop()
