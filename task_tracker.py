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
        "created_at": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")
    
def main():
    initialize_tasks_file()
    
    if len(sys.argv) < 3:
        print("Usage: python task_tracker.py add \"Task description\"")
        return
    
    command = sys.argv[1]
    if command == "add":
        description = "".join(sys.argv[2:])
        add_task(description)
    else:
        print("Invalid Command!")

if __name__ == "__main__":
    main()