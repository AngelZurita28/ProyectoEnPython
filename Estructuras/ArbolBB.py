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

    def eliminar(self, dato):
        raiz = self.eliminarr(dato)

    def eliminarr(self, raiz, dato):
        if raiz is None:
            return raiz
        if dato > raiz.dato:
            raiz.izquierdo = self.eliminarr(raiz.izquierdo, dato)
            return raiz
        if dato < raiz.dato:
            raiz.derecho = self.eliminarr(raiz.derecho, dato)
            return raiz
        if raiz.izquierdo is None and raiz.derecho is None:
            raiz = None
            return raiz
        if raiz.izquierdo is None and raiz.derecho is not None:
            raiz = raiz.derecho
            return raiz
        if raiz.izquierdo is not None and raiz.derecho is None:
            raiz = raiz.izquierdo
            return raiz

        nodoDeValorMinimo = self.obtenerValorMinimo(raiz.derecho)
        raiz.dato = nodoDeValorMinimo.dato
        raiz.derecho = self.eliminar(raiz.derecho, nodoDeValorMinimo.dato)

    def obtenerValorMinimo(self, raiz):
        nodoActual = raiz
        while nodoActual is not None and nodoActual.izquierdo is not None:
            nodoActual = nodoActual.izquierdo
        return nodoActual

    def inorden(self):
        cadena = ""
        self.inordenr(self.raiz)

    def inordenr(self, rama):
        if rama is not None:
            self.inordenr(rama.izquierdo)
            print(str(rama.dato))
            self.inordenr(rama.derecho)

    def preorden(self):
        self.preordenr(self.raiz)

    def preordenr(self, rama):
        if rama is not None:
            print(str(rama.dato))
            self.preordenr(rama.izquierdo)
            self.preordenr(rama.derecho)

    def postorden(self):
        self.postordenr(self.raiz)

    def postordenr(self, rama):
        if rama is not None:
            self.postordenr(rama.izquierdo)
            self.postordenr(rama.derecho)
            print(str(rama.dato))

def mostrarDatos(arbol):
    print("Datos ordenados en inorden:..")
    arbol.inorden()
    print("Datos ordenados en preorden:..")
    arbol.preorden()
    print("Datos ordenados en postorden:..")
    arbol.postorden()

if __name__ == '__main__':
    end = 0
    arbol = Arbol()
    while end == 0:
        print("Ingrese un valor en el arbol [i para imprimir] [t para terminar programa]: ")
        dato = input()
        if dato.upper() == "T":
            mostrarDatos(arbol)
            break
        if dato.upper() == "I":
            mostrarDatos(arbol)
        else:
            arbol.insertar(dato)
