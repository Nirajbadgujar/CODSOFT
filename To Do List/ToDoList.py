import tkinter as tk

def add_task():
    task = task_var.get()
    if task:
        task_list.insert(tk.END, f"{len(task_list.get(0, tk.END))+1}] {task}")
        task_var.set("")

def mark_complete():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.itemconfig(selected_task, {"bg": "light green"})
        task_list.selection_clear(selected_task)

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")

title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 18))
title_label.pack(pady=10)

task_var = tk.StringVar()
task_entry = tk.Entry(root, textvariable=task_var, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="dodger blue", fg="white")
add_button.pack(pady=5)

task_list = tk.Listbox(root, selectmode=tk.SINGLE, height=15, width=50, selectforeground="black")
task_list.pack()

complete_button = tk.Button(root, text="Mark as Complete", command=mark_complete, bg="green", fg="white")
complete_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="red", fg="white")
remove_button.pack(pady=5)

root.mainloop()
