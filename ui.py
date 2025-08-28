import tkinter as tk
from tkinter import messagebox
from functools import partial
import commands

def handle_update(id, title, app):
    if not title:
        messagebox.showerror(title="Edit Task", message="Caanot update with empty task!", parent=app)
    else:
        commands.update_task({"title": title})
        update_task_frame(app)

def handle_delete(id, app):
    commands.delete_task(id)
    show_all_tasks_frame(app)
    print(id)

def submit_task(title, app):
    if not title:
        messagebox.showerror(
            title="Add Task", message="Cannot add empty task!", parent=app)
    else:
        commands.save_task({"title": title})
        show_all_tasks_frame(app)

def show_edit_task_frame(task, app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    label = tk.Label(master=frame, text=f"Edit Task: {task["title"]}")
    label.grid()
    # Add an entry widget and show the task title in it
    entry = tk.Entry(master=frame)
    entry.insert(0, task["title"])
    entry.grid()
    btn = tk.Button(master=frame, text="Submit", 
                    command=lambda: submit_task(entry.get(), app))
    btn.grid()
    # Add a button with text update for saviong the changes.

    frame.tkraise()

def update_task_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0,column=0, sticky="nsew", padx=10, pady=10)

    entry = tk.Entry(master=frame)
    entry.grid()

    update = tk.Frame(master=frame)
    update.btn = tk.Button(master=frame, text="Update", 
                           command=partial(show_edit_task_frame, app))
    update.grid(row=0,column=1)

    #command=partial(show_edit_task_frame, task, app)
    # Add a button with Back / Cancel to remove frame
    cancel = tk.Frame(master=frame)
    cancel_btn = tk.Button(master=frame, text="Cancel", command=lambda: frame.destroy)
    cancel.grid(row=0,column=2)

    frame.tkraise()

def show_add_task_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0,column=0, sticky="nsew", padx=10, pady=10)

    label = tk.Label(master=frame, text="What do you want to do?")
    label.grid()
    entry = tk.Entry(master=frame)
    entry.grid()
    btn = tk.Button(master=frame, text="Submit", 
                    command=lambda: submit_task(entry.get(), app))
    btn.grid()

    frame.tkraise()
    
def show_all_tasks_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx= 10, pady=10)

    tasks = commands.get_tasks().to_list()
    for task in tasks:
        checkbtn = tk.Checkbutton(master=frame, text=task["title"])
        checkbtn.grid(row=tasks.index(task), column=0)

        edit_btn = tk.Button(master=frame, text="Edit", 
                             command=partial(show_edit_task_frame, task, app))
        edit_btn.grid(row=tasks.index(task), column=1)

        delete_btn = tk.Button(master=frame, text="Delete", 
                               command=partial(handle_delete, task["_id"], app))
        delete_btn.grid(row=tasks.index(task), column=2)

    add_btn = tk.Button(master=frame, text= "Add Task", 
                        command=lambda: show_add_task_frame(app))
    add_btn.grid(row=len(tasks) + 1, column=1)

    frame.tkraise()