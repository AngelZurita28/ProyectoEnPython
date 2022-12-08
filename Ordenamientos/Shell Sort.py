import random


def ordenar(arr):
    salto = sw = aux = e = 0
    salto = tamano / 2
    salto = int(salto)
    while salto > 0:
        sw = 1
        while sw != 0:
            sw =0
            e = 1
            while e <= (tamano-salto):
                if arreglo[(e-1)] > arreglo[((e-1) + salto)]:
                    aux = arreglo[((e-1) + salto)]
                    arreglo[((e-1) + salto)] = arreglo[(e-1)]
                    arreglo[(e-1)] = aux
                    sw = 1
                e = e + 1
        salto = salto / 2
        salto = int(salto)

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
        print(str(item))

