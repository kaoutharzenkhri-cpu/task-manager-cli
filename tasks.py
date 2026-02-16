import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title == "":
        print("Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added!")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        print(f"{i + 1}. [{status}] {task['title']}")
    print()

def mark_done(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            return
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

