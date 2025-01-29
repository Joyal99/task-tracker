import json
import os

# File to store tasks
TASK_FILE = 'tasks.json'

# Initialize the tasks file if it doesn't exist

def initialize_tasks_file():
    if not os.path.exists(TASK_FILE) or os.stat(TASK_FILE).st_size == 0:
        with open(TASK_FILE, 'w') as f:
            json.dump([], f)
            
# Run Initialization
initialize_tasks_file()
print("Task file successfully initialized!")