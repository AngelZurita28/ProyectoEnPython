from Nodo import *

class Cola:
    head = Nodo()

    def __init__(self):
        self.head = None

    def insertar(self, dato):
        n = Nodo()
        n.dato = dato
        if self.head is None:
            self.head = n
            return
        h = self.head
        while h.siguiente is not None:
            h = h.siguiente
        h.siguiente = n

    def eliminar(self):
        if self.head is None:
            return
        if self.head.siguiente is None:
            self.head = None
            return
        self.head = self.head.siguiente

    def imprimircola(self):
        h = self.head
        cadena = ""
        while h is not None:
            cadena += h.imprimirNodo() + " "
            h = h.siguiente
        return cadena


if __name__ == "__main__":
    cola = Cola()
    while True:
        print("agrege un dato a la cola.. [i para imprimir]")
        dato = input()
        if dato.lower() == "i":
            print(cola.imprimircola())
            print("desea eliminar algun dato?... [s/n]")
            r = input()
            if r == "s":
                cola.eliminar()
                print(cola.imprimircola())
        else:
            cola.insertar(dato)

