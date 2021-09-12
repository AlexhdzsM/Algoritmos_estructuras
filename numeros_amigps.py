#Descubrir si una pareja de numeros son amigos o no

num1 = int(input("Introduzca el primer numero: "))
num2 = int(input("introduzca el segundo numero: "))

div1 = 0
div2 = 0
amigos = False

for i in range (1,num1):
    if (num1 % i == 0):
        div1 = div1 + i

for i in range (1,num2):
    if (num2 % i == 0):
        div2 = div2 + i

if (div1 == num2) and (div2 == num1):
    amigos = True

print(amigos)