import random


def ordenamientoSeleccion(datos, tamanoO):
    contador = 0
    comparaciones = 0
    intercambios = 0
    i = 0
    j = 0
    tamano = tamanoO
    minimo = 0
    aux = 0
    while i < tamano:
        contador = contador + 1
        minimo = i
        j = i + 1
        while j < tamano:
            comparaciones = comparaciones + 1
            if datos[j] < datos[minimo]:
                minimo = j
            intercambios = intercambios + 1
            j = j + 1
        aux = datos[i]
        datos[i] = datos[minimo]
        datos[minimo] = aux
        i = i + 1
    for item in datos:
        print(str(item))


if __name__ == "__main__":
    datos = []
    tamano = int(input())
    j = 0
    while j < tamano:
        datos.append(random.randint(0, 100))
        j = j + 1
    cadena = ""
    for item in datos:
        cadena += str(item) + ", "
    print(cadena)
    ordenamientoSeleccion(datos, tamano)
