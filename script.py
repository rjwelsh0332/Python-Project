def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How may task you want to add: "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            print("\nTasks:")
            if not tasks:
                print("No tasks added!")
            else:
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "In Progress"
                    print(f"{index + 1}. {task['task']} - {status}")

        #Add marking as in progress
        elif choice == '3':
            if not tasks:
                print("No tasks to edit.")
                continue

            task_edit = int(input("Enter the task to edit: ")) - 1
            if 0 <= task_edit < len(tasks):
                print("Editing Choices:")
                print("1. Mark as In Progress")
                print("2. Mark as Done")
                edit_choice = int(input("Enter your choice: "))
                if edit_choice == 1:
                    tasks[task_edit]["done"] = False
                    print("Marked as In Progress!")
                elif edit_choice == 2:
                    tasks[task_edit]["done"] = True
                    print("Marked as Done!")
                else:
                    print("Invalid Choice")
            else:
                print("Invalid task number")


        #deleting a task
        elif choice == '4':
            if not tasks:
                print("No tasks to delete.")
                continue

            remove_task = int(input("Enter the task to remove: ")) - 1
            if 0 <= remove_task < len(tasks):
                del tasks[remove_task]
                print("Task removed!")
            else:
                print("Invalid task.")


        elif choice == '5':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()