import json
import os

DATA_FILE = "data/tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(name):
    """Add a new task to the list."""
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "name": name})
    save_tasks(tasks)

def delete_task(task_id):
    """Delete a task by its ID."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)

def update_task(task_id, new_name):
    """Update task name by its ID."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["name"] = new_name
            break
    save_tasks(tasks)
