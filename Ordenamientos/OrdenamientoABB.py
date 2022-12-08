import random


class NodoABB:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class Arbol:
    raiz = NodoABB

    def __init__(self):
        self.raiz = None

    def insertar(self, nuevodato):
        self.raiz = self.insertarr(self.raiz, nuevodato)

    def insertarr(self, raiz, nuevodato):
        if raiz is None:
            raiz = NodoABB(nuevodato)
            return raiz
        if raiz.dato > nuevodato:
            raiz.izquierdo = self.insertarr(raiz.izquierdo, nuevodato)
            return raiz
        if raiz.dato < nuevodato:
            raiz.derecho = self.insertarr(raiz.derecho, nuevodato)
            return raiz
        return raiz

    def inorden(self):
        cadena = ""
        self.inordenr(self.raiz, cadena)

    def inordenr(self, rama, cadena):
        if rama is not None:
            self.inordenr(rama.izquierdo, cadena)
            print(str(rama.dato))
            self.inordenr(rama.derecho, cadena)


if __name__ == '__main__':
    arbol = Arbol()
    datos = []
    tamano = int(input())
    i = 0
    while i < tamano:
        datos.append(random.randint(-100, 100))
        i = i + 1
    for j in datos:
        arbol.insertar(j)
    for j in datos:
        print("datos sin ordenar" + str(j))
    arbol.inorden()

