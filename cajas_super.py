from collections import deque

#Creacion de las cajas
def create(n):
    global cajas
    cajas = []
    for i in range(0, n):
        box = deque()
        cajas.append(box)
        
    return cajas

#Operaciones
def new_client():
    position = int(input("En que caja se formó el cliente? "))
    pos = position - 1 
    name = input("nombre del cliente: ")
    aux = deque(cajas[pos])
    aux.append(name)
    cajas[pos] = aux
    

def bye():
    position = int(input("En que caja se atendió al cliente?  "))
    pos = position - 1 
    aux = deque(cajas[pos])
    aux.popleft()
    cajas[pos] = aux
    

def show():
    print("1 = Seleccionar una caja en especifico")
    print("2 = Ver todas las cajas")
    w = int(input("Que desea hacer? "))

    if w == 1:
        box = int(input("Que caja desea ver? "))
        print(cajas[box - 1])

    else:
        print(cajas)


# Programa
run = 1
n = int(input("¿Cuantas cajas tiene el centro comercial?: "))
create(n)

while run:
    print("------MENU------")
    print("1.- Agregar cliente a fila")
    print("2.- Se atendió a un cliente")
    print("3.- Mostrar estado de una o varias filas")
    accion = int(input("¿Que desea hacer?: "))

    if accion == 1:
        new_client()
    elif accion == 2:
        bye()
    elif accion == 3:
        show()
    else:
        print("--------Por favor elija una de las opciones-----------")

    run = int(input("presiones 1 para realizar otra accion, presione 0 para salir  "))