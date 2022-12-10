from Nodo import *


class Pila:
    top: Nodo

    def __init__(self):
        self.top = None

    def insertar(self, dato):
        n = Nodo()
        n.dato = dato
        if self.top is None:
            self.top = n
            return
        n.siguiente = self.top
        self.top = n

    def imprimir(self):
        t = self.top
        cadena = ""
        while t is not None:
            cadena += t.imprimirNodo() + " "
            t = t.siguiente
        return cadena

if __name__ == '__main__':
    p: Pila = Pila()
    while True:
        print("Ingresa un numero: ")
        dato = input()
        if dato.upper() == "i":
            print(p.imprimir())
        else:
            p.insertar(dato)
            print(p.imprimir())
