import random


def ordenar(arr):
    n = tamano
    i = 0
    while i < n:
        key = arreglo[i]
        j = i -1
        while j >= 0 and arreglo[j] > key:
            arreglo[j + 1] = arreglo[j]
            j = j - 1
        arreglo[j + 1] = key
        i = i + 1


if __name__ == '__main__':
    arreglo = []
    tamano = int(input())
    llenar = 0
    while llenar < tamano:
        arreglo.append(random.randint(0, 100))
        llenar = llenar + 1
    cadenaDesordenada = ""
    for item in arreglo:
        cadenaDesordenada += str(item) + " "
    print(cadenaDesordenada)
    ordenar(arreglo)
    for item in arreglo:
        print(str(item) + " ")
