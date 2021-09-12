array = [2, 4, 5, 65, 76, -2, 12, 11, 9, 1, 0]
size = len(array)

print(array)
aux = 0
for i in range(1, size):
    
    for j in range(0, i):
        if array[i]<array[j]:
            aux = array[i]
            array[i] = array[j]
            array[j]= aux

print(array)