from password_generator import *
from security import *
from storage import *
from access import *
"""CONTROL DEL PROGRAMA"""

def main():
    while True:
        choice = input("Ingrese el numero de la accion!\n   1. Registrarme\n    2.Logearme\n    3.Salir\n   Numero : ")
        if choice == 1:
            print(register())
        elif choice == 2:
            print(login())
        elif choice == 3:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida, vuelva a intentar!!")

if __name__ == "__main__":
    main()