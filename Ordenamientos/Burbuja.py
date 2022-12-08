import random


def burbuja(n):
    contador2 = 0
    comparaciones = 0
    recorrido = 1
    actual = 0
    cadena = ""
    while recorrido < n:
        contador2 = contador2 + 1
        u = n - recorrido
        while actual < u:
            if vector[actual] > vector[actual + 1]:
                aux = vector[actual]
                vector[actual] = vector[actual + 1]
                vector[actual + 1] = aux
            comparaciones = comparaciones + 1
            actual = actual + 1
        recorrido = recorrido + 1
    for item in vector:
        cadena += str(item) + ", "
    print(cadena)


if __name__ == '__main__':
    vector = []
    tamano = int(input())
    llenar = 0
    while llenar < tamano:
        vector.append(random.randint(1, 101))
        llenar = llenar + 1
    cadena = ""
    for item in vector:
        cadena += str(item) + ", "
    print(cadena)
    burbuja(tamano)
