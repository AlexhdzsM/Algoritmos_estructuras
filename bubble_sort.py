#Algpritmo de ordenado Bubble Sort (Intercambio)
"""Consiste en ordenar cambiando posiciones con el sgiguiente 
elemento de la lista en caso de que
este sea mayor o menor, dependiendo del caso"""

array = [1, -4, 54, 27, -6, 10, 13, 34, 55, 32, 23, 3]
print(array)

size=len(array)
aux = 0
orden = False

while orden == False:

    orden = True
    for i in range(0, size-1):
        if (array[i] > array[i+1]):
            aux = array[i+1]
            array[i+1] = array[i]
            array[i] = aux

            orden = False
           
    #print(array)
    size = size -1
print(array)