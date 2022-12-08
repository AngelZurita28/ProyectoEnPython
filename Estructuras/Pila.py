
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def imprimirNodo(self):
        return self.dato + ", "

class Pila:
    top = Nodo

    def __init__(self):
        self.top = None

    def insertar(self, n):
        if self.top is None:
            self.top = n
            return
        n.siguiente = self.top
        self.top = n

    def imprimir(self):
        t = self.top
        cadena = ""
        while t is not None:
            cadena += t.imprimirNodo()
            t = t.siguiente
        return cadena

if __name__ == '__main__':
    end = 0
    p: Pila = Pila()
    while end == 0:
        print("Ingresa un numero: ")
        dato = input()
        if dato.upper() == "i":
            print(p.imprimir())
        else:
            n = Nodo(dato)
            p.insertar(n)
            print(p.imprimir())
