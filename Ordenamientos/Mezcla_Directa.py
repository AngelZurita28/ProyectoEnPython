import random


def merge_sort(lista):
    
   if len(lista) < 2:
      return lista
   else:
        middle = len(lista) // 2
        right = merge_sort(lista[:middle])
        left = merge_sort(lista[middle:])
        return merge(right, left)

def merge(lista1, lista2):
    
    i, j = 0, 0 
    result = [] 
 
   
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
 
 
    result += lista1[i:]
    result += lista2[j:]
 
  
    return result

if __name__ == '__main__':
    lista = []
    tamano = int(input())
    llenar = 0
    while llenar < tamano:
        lista.append(random.randint(0, 100))
        llenar = llenar + 1
    cadenaSinOrdenar = ""
    for item in lista:
        cadenaSinOrdenar += str(item) + " "
    print(cadenaSinOrdenar)
    merge_sort_result = merge_sort(lista)
    print(merge_sort_result)
