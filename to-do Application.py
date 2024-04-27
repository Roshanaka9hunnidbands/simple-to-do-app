class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("Task added successfully.")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

    def show_tasks(self):
        print("Tasks:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {'[X]' if task['completed'] else '[ ]'} {task['task']}")


def main():
    todo_list = ToDoList()

    while True:
        print("\nSelect an option:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_task_completed(task_index)
        elif choice == "3":
            task_index = int(input("Enter the index of the task to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "4":
            todo_list.show_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
