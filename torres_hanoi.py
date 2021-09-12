"""
n = numero de discos
org = origen
dest = destino
aux = auxiliar
"""
def hanoi(n, org, dest, aux):
    if n > 0:
        hanoi(n-1, org, aux, dest)
        print ("se movió el disco de la posición: " + str(org) + " a la posición: " + str(dest))
        hanoi(n-1, aux, dest, org)

hanoi(3, 1, 3, 2)