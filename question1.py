"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""
import sys
def main(num_supports, total_load):
    load_per_support = total_load / num_supports
    while True:
        try:
            total_load = (input())
            break
        except ValueError:
            print("Necesito un entero")
        except EOFError:
            print("¡No se pudo completar la solicitud!")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero! Supports must be greater than zero.")
        break
    while True:
        try:
            num_supports = (input())
            break
        except ValueError:
            print("Error: Invalid input! Enter numeric values only.")
        except EOFError:
            print("Error: Invalid input! Enter numeric values only.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero! Supports must be greater than zero.")
        break
    print(f"Load per support point <{load_per_support}> N")