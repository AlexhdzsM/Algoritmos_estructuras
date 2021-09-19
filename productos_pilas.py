from random import randint
#Creacion de las pilas vacias
def create(n):
    global pilas
    pilas = []
    for i in range(0, n):
        articulo = []
        pilas.append(articulo)
        
    return pilas

#Operaciones
def add(index, times):
    pos = index -1
    for i in range(0,times):
        sn = randint(0,1000)
        aux = pilas[pos]
        aux.append(sn)
        pilas[pos] = aux
    

def remove(index, times):
    pos = index -1
    for i in range(0,times):
        aux = pilas[pos]
        aux.pop()
        pilas[pos] = aux

    

def show():
    print(pilas)

#Programa
n = int(input("Cantidad de productos que habrá: "))
create(n)
run = 1
while run:

    print("----MENU-----")
    print("1.- agregar articulo")
    print("2.- eliminar articulo")
    print("3.- Mostrar articulos")
    print("4.- exit")

    action = int(input("Seleccione el numero de la accion quer desea realizar: "))

    if action == 1:
        cat = int(input("En que categoria desea agregar el producto: "))
        t = int(input("Cuantos elementos desea agregar: "))
        add(cat, t)
        
    elif action == 2:
        cat = int(input("de que categoria desea eliminar el producto: "))
        t = int(input("Cuantos elementos desea eliminar: "))
        remove(cat, t)

    elif action == 3:
        show()

    elif action == 4:
        run = 0

