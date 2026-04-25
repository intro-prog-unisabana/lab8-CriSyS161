"""Laboratorio 8 - CLI del gestor de tareas."""
import sys
from todo_manager import read_todo_file, write_todo_file
def main():
    try:
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
            else:
                raise ValueError("Command not found!")
        print(f"Arguments received: {sys.argv[1:]}")
        tasks = read_todo_file(file_path)
        print(f"Tasks in list: {tasks}")
    except (IndexError, ValueError) as x:
        print(f"{x}")
    except Exception as x:
        print(f"An unexpected error ocurred: {x}")
if __name__ == "__main__":
    main()

