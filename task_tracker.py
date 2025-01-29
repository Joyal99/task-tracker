import json
import sys
import os
from datetime import datetime

# File to store tasks
TASK_FILE = 'tasks.json'

# Initialize the tasks file if it doesn't exist
def initialize_tasks_file():
    if not os.path.exists(TASK_FILE) or os.stat(TASK_FILE).st_size == 0:
        with open(TASK_FILE, 'w') as f:
            json.dump([], f)

def load_tasks():
    with open(TASK_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    task_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def list_tasks(status=None):
    """List tasks optionally filtered by status."""
    tasks = load_tasks()

    if status:
        tasks = [task for task in tasks if task["status"] == status]

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} "
              f"(Created: {task['created_at']}, Updated: {task.get('updated_at', 'N/A')})")
        
def update_task(task_id, new_description):
    """Updating the description of a task."""
    tasks= load_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updated_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
        
    print(f"Task {task_id} not found.")
    
def mark_task(task_id, status):
    """Updating the statu of a task(todo, in-progress, done)."""
    valid_statuses = ["todo", "in-progress", "done"]
    
    if status not in valid_statuses:
        print(f"Invalid status. Choose from: {', '.join(valid_statuses)}")
        return
    
    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updated_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}.")
            return
        
    print(f"Task {task_id} not found.")

def main():
    initialize_tasks_file()

    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py <command> [options]")
        return

    command = sys.argv[1]

    if command == "add":
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "list":
        if len(sys.argv) > 2:
            status = sys.argv[2]
            list_tasks(status)
        else:
            list_tasks()
    elif command == "update":
        if(len(sys.argv) < 4):
            print("Usage: python task_tracker.py update <task_id> \"New description\"")
        else:
            try:
                task_id = int(sys.argv[2])
                new_description = " ".join(sys.argv[3:])
                update_task(task_id, new_description)
            except ValueError:
                print("Invalid task ID. Please provide a valid task ID.")
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage:python task_tracker.py mark-in-progress <task_id>")
        else:
            try:
                task_id = int(sys.argv[2])
                mark_task(task_id, "in-progress")
            except ValueError:
                print("Invalid task ID. Please provide a valid task ID.") 
    elif command == "mark-done":
        if len(sys.argv) < 3:
                print("Usage: python task_tracker.py mark-done <task_id>")
        else:
            try:
                task_id = int(sys.argv[2])
                mark_task(task_id, "done")
            except ValueError:
                print("Invalid task ID. Please provide a valid task ID.")
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
