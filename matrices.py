import numpy as np

matriz1 = np.zeros((3,3))
matriz2 = np.zeros((3,3))

#Llenar matrices
def llenado(matriz):
    for i in range (0, 3):
        for j in range(0,3):
            matriz[i,j] = int(input("introduzca el valor de la fila " + str(i) + " y la columna " + str(j) + ":" ))


print("Ahora introducirá los datos para las matrices")

llenado(matriz1)
llenado(matriz2)

print(matriz1)
print("---------------------")
print(matriz2)

matriz_res = np.dot(matriz1, matriz2)
print(matriz_res)