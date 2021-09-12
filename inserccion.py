from datetime import datetime
array = [2, 4, 5, 65, 76, -2, 12, 11, 9, 1, 0]
size = len(array)
print(array)



for i in range(1, size):
    aux = array[i]
    j = i-1
    k = j
    for j in range(0,(i)):

        if (array[k]>aux):
        
            array[k+1]=array[k]
            k = k-1

    array[k+1] = aux

print(array)

hora =datetime.now()
print(hora)