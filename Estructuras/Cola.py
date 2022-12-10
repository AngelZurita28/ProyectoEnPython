from Nodo import *

class Cola:
    head = Nodo

    def __init__(self):
        self.head = None

    def insertar(self, n):
        if self.head is None:
            self.head = n
            return
        h = self.head
        while h.siguiente is not None:
            h = h.siguiente
        h.siguiente = n

    def imprimir(self):
        h: Nodo = self.head
        cadena = ""
        while h is not None:
            cadena += h.imprimirNodo()
            h = h.siguiente
        return cadena
