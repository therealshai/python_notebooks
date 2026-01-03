class Task:
    STATES = ("New", "In Progress", "Completed")

    def __init__(self, name, state="New"):
        if state not in Task.STATES:
            raise ValueError("Invalid task state")
        self.name = name
        self.state = state

    def update_state(self, new_state):
        if new_state not in Task.STATES:
            raise ValueError("Invalid task state")
        self.state = new_state

    def __str__(self):
        return f"{self.name} — {self.state}"

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, name, state="New"):
        if name in self.tasks:
            raise ValueError("Task already exists")
        self.tasks[name] = Task(name, state)

    def update_task(self, name, new_state):
        if name not in self.tasks:
            raise ValueError("Task not found")
        self.tasks[name].update_state(new_state)

    def get_tasks(self):
        return list(self.tasks.values())
