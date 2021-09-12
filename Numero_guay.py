#Descubrir si un numero es guay o no

num = int(input("Introduzca el numero que desea saber si es guay: "))
sum = 0
guay = False

for i in range (1, num):
    if sum < num:
        sum = sum + i
if sum == num:
    guay = True

print(guay)