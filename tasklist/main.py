from Task import TaskManager
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
manager = TaskManager()
selected_task_index = None

def add_task():
    name = task.get().strip()
    state = status.get()

    if not name:
        messagebox.showinfo("Information", "Task name cannot be empty")
        return

    try:
        manager.add_task(name, state)
        refresh_task_list()
        task.set("")          # clear entry
        status.set("New")     # reset dropdown
    except Exception as err:
        messagebox.showinfo("Information", "{}".format(err))


def refresh_task_list():
    task_listbox.delete(0, END)   # clear UI list

    for task in manager.get_tasks():
        task_listbox.insert(END, str(task))

def on_task_select(event):
    global selected_task_index

    selection = task_listbox.curselection()
    if not selection:
        return

    selected_task_index = selection[0]
    task_obj = manager.get_tasks()[selected_task_index]

    task.set(task_obj.name)
    status.set(task_obj.state)


def update_task():
    if selected_task_index is None:
        messagebox.showinfo("Information", "Select a task to update")
        return

    new_state = status.get()
    task_obj = manager.get_tasks()[selected_task_index]

    try:
        task_obj.update_state(new_state)
        refresh_task_list()
    except Exception as err:
        messagebox.showinfo("Information", "{}".format(err))

root = Tk() # root parent class
style = ttk.Style()
style.theme_use("default")

BASE_BG = "#f5f5f5"
TEXT_COLOR = "#333333"
ACCENT = "#4CAF50"

style.configure(
    "TFrame",
    background=BASE_BG
)

style.configure(
    "TLabel",
    background=BASE_BG,
    foreground=TEXT_COLOR,
    font=("Segoe UI", 11)
)

style.configure(
    "Header.TLabel",
    font=("Segoe UI", 14, "bold"),
    foreground="#222222"
)

style.configure(
    "TEntry",
    font=("Segoe UI", 11),
    padding=6
)

style.configure(
    "TCombobox",
    font=("Segoe UI", 11),
    padding=4
)

style.configure(
    "Accent.TButton",
    font=("Segoe UI", 11, "bold"),
    padding=(12, 8)
)


root.title("Shai's Tasklist ") #title of the frame
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (WINDOW_WIDTH // 2)
y = (screen_height // 2) - (WINDOW_HEIGHT // 2)

root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
root.resizable(False, False)


mainframe = ttk.Frame(root, padding=(15, 15, 15, 15))

mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

task= StringVar() #store task here

#task field
task_field= ttk.Entry(mainframe, textvariable=task)
task_field.grid(column=1, row=1, sticky=(W, E))
#task_field.pack(fill=X, side=TOP, ipadx=5, ipady=5)
task_field.focus()

ok_button = ttk.Button(mainframe, text="OK",style="Accent.TButton", command=add_task)
ok_button.grid(column=2, row=1, sticky=(W, E))
ok_button.bind("<Return>", add_task)


#label - task
task_list_name= StringVar()
task_list_name.set("Task left to compelte")
task_list_label = ttk.Label(
    mainframe,
    textvariable=task_list_name,
    style="Header.TLabel"
)

task_list_label.grid(column=1, row=2, sticky=(W, E))

task_listbox = Listbox(
    mainframe,
    height=10,
    bg="#ffffff",
    fg=TEXT_COLOR,
    selectbackground=ACCENT,
    selectforeground="white",
    font=("Segoe UI", 14),
    relief="solid",
    borderwidth=1
)


task_listbox.grid(column=1, row=4, columnspan=2, sticky=(W, E))
task_listbox.bind("<<ListboxSelect>>", on_task_select)


task_list=StringVar()

status= StringVar()
states = ("New", "In Progress", "Completed")
status_dropdown = ttk.Combobox(mainframe,
                               textvariable=status,
                               values=states,
                               state="readonly")
status_dropdown.grid(column=1, row=3, sticky=(W, E))
status.set("New")

status_dropdown.bind("<Return>", add_task)

update_button = ttk.Button(mainframe, text="Update", command=update_task)
update_button.grid(column=2, row=3, sticky=(W, E))

task_field.grid(padx=5, pady=5)
ok_button.grid(padx=5, pady=5)

for child in mainframe.winfo_children():
    child.grid_configure(padx=8, pady=6)

root.mainloop()