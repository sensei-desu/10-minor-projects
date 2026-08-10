

def todo_app():
    tasks = []
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. View Tasks | 2. Add Task | 3. Delete Task | 4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            if not tasks:
                print("Your list is empty!")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
        elif choice == '2':
            task = input("Enter new task: ")
            tasks.append(task)
            print("Task added!")
        elif choice == '3':
            num = int(input("Enter task number to delete: "))
            if 0 < num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed: '{removed}'")
            else:
                print("Invalid task number.")
        elif choice == '4':
            break

if __name__ == "__main__":
    todo_app()
