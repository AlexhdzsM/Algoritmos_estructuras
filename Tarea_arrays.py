"""Debes recorrer un array con números decimales y al finalizar mostrar por pantalla los siguientes datos

- El número mayor encontrado en el array

- El número menor encontrado en el array

- El valor promedio de entre los números de todo el array"""

array = []
size = int(input("Cuantos elementos conformaran la lista?: "))

for i in range(0,size):
    array.append(float(input("Introduzca un valor: ")))

mayor = array[0]
menor = array[0]
suma = 0

for i in range(0,size):
    if mayor < array[i]:
        mayor = array[i]

    if menor > array[i]:
        menor = array[i]
    
    suma = suma + array[i]

promedio = suma/size

print("El numero mayor es: " + str(mayor))
print("el numero menor es: " + str(menor))
print("el promedio es: " + str(promedio))