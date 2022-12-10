from Nodo import *


class Lista:
    head: Nodo

    def __init__(self):
        self.head = None

    def insertar(self, dato):
        nuevo = Nodo()
        nuevo.dato = dato
        if self.head is None:
            self.head = nuevo
            return
        if nuevo.dato < self.head.dato:
            nuevo.siguiente = self.head
            self.head = nuevo
            return
        h = self.head
        while h.siguiente is not None:
            if h.siguiente.dato > dato:
                break
            h = h.siguiente
        nuevo.siguiente = h.siguiente
        h.siguiente = nuevo

    def eliminar(self, dato):
        if self.head.dato == dato:
            self.head = self.head.siguiente
            return
        if self.head.dato > dato:
            return
        h = self.head
        while h.siguiente is not None:
            if h.siguiente.dato == dato:
                break
            h = h.siguiente
        h.siguiente = h.siguiente.siguiente

    def imprimir(self):
        h = self.head
        cadena = ""
        while h is not None:
            cadena += h.imprimirNodo() + " "
            h = h.siguiente
        return cadena

if __name__ == "__main__":
    lista = Lista()
    while True:
        print("agrege un dato a la cola.. [i para imprimir]")
        dato = input()
        if dato.lower() == "i":
            print(lista.imprimir())
            print("desea eliminar algun dato?... [s/n]")
            r = input()
            if r == "s":
                print("que dato desea eliminar?...")
                lista.eliminar(input())
                print(lista.imprimir())
        else:
            lista.insertar(dato)

