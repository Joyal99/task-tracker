import json
import sys
import os
from datetime import datetime

# File to store tasks
TASK_FILE = 'tasks.json'

# ANSI Escape Codes for Colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
BOLD = "\033[1m"

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
    """Add a new task."""
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
    print(f"{GREEN}Task added successfully (ID: {task_id}){RESET}")

def list_tasks(status=None):
    """List tasks optionally filtered by status."""
    tasks = load_tasks()

    if status:
        tasks = [task for task in tasks if task["status"] == status]

    if not tasks:
        print(f"{RED}No tasks found.{RESET}")
        return

    for task in tasks:
        status_color = GREEN if task["status"] == "done" else YELLOW if task["status"] == "in-progress" else CYAN
        print(f"{BOLD}[{task['id']}] {task['description']} {RESET}- {status_color}{task['status'].upper()}{RESET} "
              f"(Created: {task['created_at']}, Updated: {task.get('updated_at', 'N/A')})")
        
def update_task(task_id, new_description):
    """Update the description of a task."""
    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updated_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"{YELLOW}Task {task_id} updated successfully!{RESET}")
            return
    
    print(f"{RED}Error: Task {task_id} not found. Cannot update.{RESET}")
    
def mark_task(task_id, status):
    """Update the status of a task (todo, in-progress, done)."""
    valid_statuses = ["todo", "in-progress", "done"]
    
    if status not in valid_statuses:
        print(f"{RED}Error: Invalid status. Choose from: {', '.join(valid_statuses)}{RESET}")
        return

    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updated_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            status_color = GREEN if status == "done" else YELLOW if status == "in-progress" else CYAN
            print(f"{status_color}Task {task_id} marked as {status}.{RESET}")
            return
    
    print(f"{RED}Error: Task {task_id} not found. Cannot update status.{RESET}")

def delete_task(task_id):
    """Delete a task by its ID."""
    tasks = load_tasks()
    
    if not any(task["id"] == task_id for task in tasks):
        print(f"{RED}Error: Task {task_id} not found. Cannot delete.{RESET}")
        return

    updated_tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(updated_tasks)
    print(f"{RED}Task {task_id} deleted successfully.{RESET}")

def clear_tasks():
    """Delete all tasks from the task file."""
    confirmation = input(f"{BOLD}{RED}Are you sure you want to delete all tasks? (yes/no): {RESET}").strip().lower()
    if confirmation == "yes":
        save_tasks([])  # Save an empty list to the file
        print(f"{RED}All tasks have been deleted successfully.{RESET}")
    else:
        print(f"{GREEN}Operation canceled.{RESET}")

    
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
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py delete <task_id>")
        else:
            try:
                task_id = int(sys.argv[2])
                delete_task(task_id)
            except ValueError:
                print("Invalid task ID. Please provide a valid task ID.")
    elif command == "clear":
        clear_tasks()
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
