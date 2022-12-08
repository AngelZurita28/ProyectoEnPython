class Nodo:
    def __init__(self, dato):
        self.dato:str = dato
        self.siguiente = None

    def imprimirNodo(self):
        return self.dato + ", "
