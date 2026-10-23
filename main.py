#CLI Task Manager
import json
from datetime import date, datetime

tasks = []

def add_task(tasks):
    title = input("Enter task title: ").strip()
    print("Select priority:")
    priorities = ["High", "Medium", "Low"]
    for index, priority in enumerate(priorities, start=1):
        print(f"{index}. {priority}")
    while True:
        try:
            choice = int(input("Enter the task priority: ").strip())
            if 1 <= choice <= len(priorities):
                priority = priorities[choice - 1]
                break
            print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number")
    task = {
        "title": title,
        "completed": False,
        "priority": priority,
        "due_date": None
    }
    tasks.append(task)
    print("Task added!")
    
def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task['title']} | {'Completed' if task['completed'] else 'Pending'} | {task['priority']} | {task['due_date']} ")
    print()
        
def complete_task(tasks):
    try:
        number = int(input("Which number task did you complete: ")) - 1
        tasks[number]["completed"] = True
    except ValueError:
        print("Please enter a valid number")
        
def delete_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Which task to delete: ")) - 1
        tasks.pop(number)
    except ValueError:
        print("Please enter a valid number")
    save_tasks(tasks)
    
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    print("Task Saved!")

def filter_task(tasks):
    pass
   
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def edit_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Which task did you want to edit: "))-1
        add_task(tasks)[number]
        print("Task was Updated")
    except ValueError:
        print("Please enter a valid number")
        
tasks = load_tasks()
        

while True:
    print("================================")
    print("TASK MANAGER")
    print("================================")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Complete task")
    print("4. Edit task")
    print("5. Delete task")
    print("6. Filter tasks")
    print("7. Exit")
    print()
    print("================================")
    print("Choose an option:")
    
    
    choice = input("Choose an option: ")
    if choice == "1":
        add_task(tasks)
        save_tasks(tasks)
    elif choice == "2":
        print("Index. Title | Completion | Priority | Due_Date")   
        show_tasks(tasks)
    elif choice == "3":
        complete_task(tasks)
        save_tasks(tasks) 
    elif choice == "4":
        edit_task(tasks)          
    elif choice == "5":
        delete_task(tasks)
    elif choice == "6":
        filter_task(tasks)
    elif choice == "7":
        print("Exit")
        break
    else:
        print("Invalid Input")
