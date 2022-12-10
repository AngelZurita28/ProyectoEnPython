from Nodo import *


class ColaDoble:
    head: NodoDoble
    tail: NodoDoble

    def __init__(self):
        self.head = None
        self.tail = None

    def agregarfrente(self, dato):
        nuevo = NodoDoble()
        nuevo.dato = dato
        if self.head is None:
            self.head = nuevo
            self.tail = nuevo
            return
        self.head.anterior = nuevo
        nuevo.siguiente = self.head
        self.head = nuevo

    def agregarfinal(self, dato):
        nuevo = NodoDoble()
        nuevo.dato = dato
        if self.head is None:
            self.head = nuevo
            self.tail = nuevo
            return
        self.tail.siguiente = nuevo
        nuevo.__annotations__ = self.tail
        self.tail = nuevo

    def eliminarfrente(self):
        if self.head is None:
            return
        if self.head.siguiente is None:
            self.head = None
            self.tail = None
            return
        self.head = self.head.siguiente
        self.head.anterior = None

    def eliminarfinal(self):
        if self.head is None:
            return
        if self.head.siguiente is None:
            self.head = NodoDoble()
            self.tail = NodoDoble()
            return
        self.tail = self.tail.anterior
        self.tail.siguiente = None

    def imprimirBicola(self):
        cadena = ""
        h = self.head
        if h is not None:
            cadena += h.imprimirNodo()
            h = h.siguiente
            while h is not None:
                cadena += ", " + h.imprimirNodo()
                h = h.siguiente
            return cadena
        return "La cola esta vacia"

if __name__ == "__main__":
    cola = ColaDoble()
    while True:
        print("agrege un dato a la cola.. [i para imprimir]")
        dato = input()
        if dato.lower() == "i":
            print(cola.imprimirBicola())
            print("desea eliminar algun dato?... [s/n]")
            r = input()
            if r == "s":
                print("Desea eliminar un dato al principio [p] o al final [f]?")
                r = input()
                if r == "p":
                    cola.eliminarfrente()
                if r == "f":
                    cola.eliminarfinal()
                print(cola.imprimirBicola())
        else:
            print("Desea agregarlo al principio [p] o al final [f] de la cola?")
            r = input()
            if r.lower() == "p":
                cola.agregarfrente(dato)
            if r.lower() == "f":
                cola.agregarfinal(dato)
