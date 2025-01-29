# 📝 Task Tracker CLI

Task Tracker CLI is a simple command-line tool to help you **manage your tasks efficiently**.  
You can **add, list, update, delete, and track** tasks using simple commands.

## 📌 Features
✅ Add a new task  
✅ List all tasks or filter by status (`todo`, `in-progress`, `done`)  
✅ Update a task’s description  
✅ Mark a task as `in-progress` or `done`  
✅ Delete a task by its ID  
✅ Clear all tasks (with confirmation)  
✅ Error handling for invalid inputs  
✅ Color-coded output for better readability  

---

## 🚀 Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/task-tracker-cli.git
cd task-tracker-cli
```

### **2️⃣ Run the Script**
Ensure you have Python 3+ installed, then run:
```sh
python task_tracker.py
```
If you see ```Usage: python task_tracker.py <command>```, it means everything is set up! 🎉

## 📖 Usage Guide
### **✅ Add a New Task**
```sh
python task_tracker.py add "Buy groceries"
```
#### **🟢 Output:**
```sh
Task added successfully (ID: 1)
```
### **✅ List All Tasks**
```sh
python task_tracker.py list
```
#### **🟡 Output:**
```sh
[1] Buy groceries - TODO (Created: 2025-01-28T10:00:00, Updated: 2025-01-28T10:00:00)
```
### **✅ List Tasks by Status**
```sh
python task_tracker.py list done
```
#### **🔵 Shows only tasks marked as done**
```sh
No tasks found.
```
### **✅ Update a Task**
```sh
python task_tracker.py update 1 "Buy groceries and cook dinner"
```
#### **🟠 Output:**
```sh
Task 1 updated successfully!
```
### **✅ Mark a Task as ```in-progress```**
```sh
python task_tracker.py mark-in-progress 1
```
#### **🟣 Output:**
```sh
Task 1 marked as in-progress.
```
### **Mark a Task as ```done```**
```sh
python task_tracker.py mark-done 1
```
#### **🟢 Output:**
```sh
Task 1 marked as done.
```
### **✅ Delete a Task**
```sh
python task_tracker.py delete 1
```
#### **🔴 Output:**
```sh
Task 1 deleted successfully.
```
### **✅ Clear All Tasks**
```sh
python task_tracker.py clear
```
#### **⚠️ Prompt:**
```sh
Are you sure you want to delete all tasks? (yes/no): yes
All tasks have been deleted successfully.
```

---

### **⚠️ Error Handling**
If you enter an invalid command, the script will warn you:
```sh
python task_tracker.py update 100 "Non-existent task"
```
#### **🔴 Output:**
```sh
Error: Task 100 not found. Cannot update.
```
---
## **🛠️ Contributing**
Feel free to fork this repo and submit pull requests! If you find a bug, open an issue.

---

## **📝 License**
This project is open-source under the MIT License.



