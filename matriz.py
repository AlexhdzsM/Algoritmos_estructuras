import numpy as np
matriz = np.empty((2,3))
matriz_zero = np.zeros((3,3))
matriz_uno = np.ones((4,4))

print(matriz)
print(matriz_zero)
print(matriz_uno)

print(matriz_uno[1,1])

matriz[0,0] = 4
matriz[1,1] = 5
print(matriz)