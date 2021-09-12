#Calcular el facrorial de un numero

num = int(input("introduzca el numero del que desea calcular el facotorial: "))

res = num

if num == 0:
    res = 1
else:
    for i in range(1, num):
        res = res * i
print(res)
