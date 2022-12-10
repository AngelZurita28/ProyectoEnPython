class Nodo:
    def __init__(self):
        self.dato = None
        self.siguiente = None

    def imprimirNodo(self):
        return self.dato


class NodoDoble:
    def __init__(self):
        self.dato = None
        self.siguiente = None
        self.anterior = None

    def imprimirNodo(self):
        return self.dato


class NodoABB:
    def __init__(self):
        self.dato:str = None
        self.derecho = None
        self.izquierdo = None