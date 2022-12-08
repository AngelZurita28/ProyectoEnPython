import random


def partition(array, low, high):
  pivot = array[high]

  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1

      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

def quickSort(array, low, high):
  if low < high:

    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)

    quickSort(array, pi + 1, high)


if __name__ == '__main__':
    vector = []
    tamano = int(input())
    llenar = 0
    while llenar < tamano:
        vector.append(random.randint(0, 100))
        llenar = llenar + 1
    cadenaDesordenada = ""
    for item in vector:
        cadenaDesordenada += str(item) + " "
    print(cadenaDesordenada)
    quickSort(vector, 0, tamano - 1)
    cadenaOrdenada = ""
    for item in vector:
        cadenaOrdenada += str(item) + " "
    print(cadenaOrdenada)
