"""Laboratorio 8 - CLI del gestor de tareas."""
import sys
from todo_manager import read_todo_file, write_todo_file
def main():
    try:
        if "--help" in sys.argv:
            print('Usage: python main.py <file_path> <command> [arguments]...')
            print('Commands:')
            print('add "task" - Add a task to the list.')
            print('remove "task" - Remove a task from the list.')
            print('view - Display all tasks.')
            return
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")
        file_path = sys.argv[1]
        tasks = read_todo_file(file_path)
        i = 2
        while i < len(sys.argv):
            command = sys.argv[i]
            if command == "view":
                print("Tasks:")
                for task in tasks:
                    print(task)
                i += 1
            elif command == "add":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "add".') 
                new_task = sys.argv[i + 1]
                tasks.append(new_task)
                print(f'Task "{new_task}" added.')
                i += 2
            elif command == "remove":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "remove".')  
                tasks_remove = sys.argv[i + 1]
                if tasks_remove in tasks:
                    tasks.remove(tasks_remove)
                    print(f'Task "{tasks_remove}" removed.')
                else:
                    print(f'Task "{tasks_remove}" not found.')
                i += 2
            else:
                raise ValueError("Command not found!")
        write_todo_file(file_path, tasks)
    except (IndexError, ValueError) as x:
        print(f"{x}")
    except Exception as x:
        print(f"An unexpected error occurred: {x}")
if __name__ == "__main__":
    main()

