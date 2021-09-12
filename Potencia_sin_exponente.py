#potencia sin elevar a la potencia
num1 = int(input("introduzca el numero que quiere elevar a x potencia: "))
num2 = int(input("introduzca la potencia a la que quiere elevar el numero anterior: "))

res = num1

if num2 == 0:
    res = 1

if num2 > 0:
    for i in range(1,num2):
        res = res * num1

if num2 < 0:
    res = 1
    for i in range(num2, 0):
        res = res/num1
    
print(res)