"""Laboratorio 8 - CLI del gestor de tareas."""
import sys
from todo_manager import read_todo_file, write_todo_file
def main():
    try:
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")
        file_path = sys.argv[1]
        print(f"Arguments received: {sys.argv[1:]}")
        tasks = read_todo_file(file_path)
        print(f"Tasks in list: {tasks}")
    except IndexError as x:
        print(f"Error: {x}")
    except Exception as x:
        print(f"An unexpected error ocurred: {x}")


# TODO: Implementar CLI según README.md
