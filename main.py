"""Laboratorio 8 - CLI del gestor de tareas."""
import sys
from todo_manager import read_todo_file, write_todo_file
def main():
    try:
        if "--help" in sys.argv:
            print("Usage: python main.py <file_path> <command> [arguments]...")
            return
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")
        file_path = sys.argv[1]
        if len(sys.argv) >= 3:
            command = sys.argv[2]
            if command == 'view':
                tasks = read_todo_file(file_path)
                print("Tasks:")
                for task in tasks:
                    print(task)
            elif command == "add":
                if len(sys.argv) < 4:
                    raise IndexError('Task description required for "add"')
                new_tasks = sys.argv[3]
                tasks = read_todo_file(file_path)
                tasks.append(new_tasks)
                write_todo_file(file_path, tasks)
                print(f'Task "{new_tasks}" added.')
            elif command == "remove":
                if len(sys.argv) < 4:
                    raise IndexError('Task description required for "remove"')
                tasks_remove = sys.argv[3]
                tasks = read_todo_file(file_path)
                if tasks_remove in tasks:
                    tasks.remove(tasks_remove)
                    write_todo_file(file_path, tasks)
                    print(f'Task "{tasks_remove}" removed.')
                else:
                    print(f'Task"{tasks_remove}" not found')
            else:
                raise ValueError("Command not found!")
    except (IndexError, ValueError) as x:
        print(f"{x}")
    except Exception as x:
        print(f"An unexpected error ocurred: {x}")
if __name__ == "__main__":
    main()

