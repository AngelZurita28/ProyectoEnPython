from Cola import *


if __name__ == '__main__':
    end = 0
    p: Cola = Cola()

    while end == 0:
        print("Ingresa un numero: ")
        dato = input()
        if dato.upper() == "i":
            print(p.imprimir())
        else:
            n = Nodo(dato)
            p.insertar(n)
            print(p.imprimir())
