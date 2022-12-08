class Nodo:
    def __init__(self, dato):
        self.dato = ""
        self.siguiente = None
        self.anterior = None

    def imprimirNodo(self):
        return self.dato


class listaDoble:
    head = Nodo
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.head = None

    def insertar(self, dato):
        h = self.head
        if self.head is None:
           n = Nodo(dato)
           self.primero = n
           self.ulimo = self.primero
           return
        n = Nodo(dato)
        self.ultimo.siguiente = n
        n.anterior = self.ultimo
        self.ultimo = n

    def imprimirLista(self):
        h = self.head
        cadena = ""
        if self.head is not None:
            while self.h.siguiente is not None:
                cadena += self.h.imprimirNodo()
        return cadena


if __name__ == '__main__':
    end = 0
    milista = listaDoble
    while end == 0:
        print("Ingrese un dato: ")
        milista.insertar(listaDoble, input())
        milista.imprimirLista()