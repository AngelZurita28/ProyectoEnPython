from Nodo import *


class listaDoble:
    head: NodoDoble
    tail: NodoDoble
    def __init__(self):
        self.head = None
        self.tail = None

    def insertar(self, dato):
        nuevo = NodoDoble()
        nuevo.dato = dato
        if self.head is None:
            self.head = nuevo
            self.tail = self.head
            return
        self.tail.siguiente = nuevo
        nuevo.anterior = self.tail
        self.tail = nuevo

    def imprimirLista(self):
        h = self.head
        cadena = ""
        while h is not None:
            cadena += h.imprimirNodo() + " "
            h = h.siguiente
        return cadena


if __name__ == '__main__':
    end = 0
    milista = listaDoble()
    while end == 0:
        print("Ingrese un dato: ")
        milista.insertar(input())
        print(milista.imprimirLista())
