#encontrar si un numero es perfecto

num = int(input("introduzca un numero para comprobar si es perfecto o no: "))
perfect = False
suma = 0

if num <= 0:
    perfect = False

else:
    for i in range(1,num):
        if (num % i == 0):
            suma = suma + i
        if suma == num:
            perfect = True

print(perfect)
