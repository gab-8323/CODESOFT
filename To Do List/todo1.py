class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = 'Completed' if self.completed else 'Not Completed'
        return f"{self.title} - {self.description} [{status}]"
tasks = []

def add_task(title, description):
    task = Task(title, description)
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks):
            print(f"{idx + 1}. {task}")

def update_task(index, title=None, description=None):
    if 0 <= index < len(tasks):
        if title:
            tasks[index].title = title
        if description:
            tasks[index].description = description
        print("Task updated successfully!")
    else:
        print("Invalid task index.")

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

def mark_task_completed(index):
    if 0 <= index < len(tasks):
        tasks[index].mark_completed()
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to update: ")) - 1
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            update_task(index, title if title else None, description if description else None)
        elif choice == '4':
            index = int(input("Enter task index to delete: ")) - 1
            delete_task(index)
        elif choice == '5':
            index = int(input("Enter task index to mark as completed: ")) - 1
            mark_task_completed(index)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
