#Restar 2 numeros sin usar resta
num1 = int(input("introduce el primer numero: "))
num2 = int(input("introduce el segundo numero: "))

count = 0

if num1 > num2:
    for i in range(num2,num1):
         num2 = num2 + 1
         count = count + 1
elif num2 > num1:
    for i in range(num1,num2):
         num1 = num1 + 1
         count = count + 1
elif num1 == num2:
    count=0

res = count

print(res)