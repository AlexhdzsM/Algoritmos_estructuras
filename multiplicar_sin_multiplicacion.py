#multiplicar 2 numeros sin usar mulriplicacion
num1 = int(input("Introduzca el primer numero: "))
num2 = int(input("Introduzca el segundo numero: "))
valor_original = num1

for i in range(1,num2):
    num1 = num1 + valor_original

print(num1)