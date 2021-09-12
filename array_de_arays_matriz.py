#Primero se crea una variable para el numero de columnas de la matriz
c = int(input("Numero de columnas: "))

#Elementos la usaremos para saber cuantas filas tendrá cada columna
elementos = []
#Matriz será la matriz final
matriz = []

#Ciclo para asignar cuantas filas tendrá cada columna
for i in range (0, c):
    elementos.append(int(input("elementos que habrá en la " + str(i) + " columna: ")))

#Funcion con la que se llenará la matriz (Se llena de columna en columna)
def llenado(columna, tamano):
    #f se usa para formar cada columna y se inserta en la matriz
    f = []
    for i in range(0, tamano):
        f.append(int(input("introduzca el valor para la columna " + str(columna) + " y fila " + str(i) + ": ")))

    matriz.append(f)

#Llamamos a la funcion tantas veces como columnas se tengan
for i in range(0, c):
    
    llenado(i,elementos[i])

print(matriz)