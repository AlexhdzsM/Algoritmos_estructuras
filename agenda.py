
meses = 12
dias =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
agenda =[]

print("------MENU-----------")
print("Opciones:")
print("para agregar una actividad selecciona 1")
print("para modificar una actividad selecciona 2")
print("para eliminar una actividad selecciona 3")
accion = int(input("¿Que deseas hacer?: "))

print("Ahora seleccione la fecha para realizar la accion")
print("Introduzca datos numericos, enero = 1, febrero = 2, etc")
mes = int(input("introduzca el mes: "))
fecha = int(input("introduzca el dia: "))

#Creacion de agenda vacia
for i in range (0, meses):
    month=[]
    for j in range(0,dias[i]):
        dia = []
        month.append(dia)

    agenda.append(month)

def mod(a, m, d):
    x = True
    if a == 1:
        day = []
        day.append(input("Actividad: "))
        
        while x:
            x = int(input("desea agregar otra actividad? 1 = si, 0 = No: "))
            if x == 0:
                x = False
                break
            day.append(input("Actividad: "))
        
        agenda[m][d] = day

    elif a == 2:
        print(agenda[m][d])
        index = int(input("Seleccione el indice de la actividad que desea cambiar: "))

        agenda[m][d][index] = input("Actividad: ")

    else: 
        print(agenda[m][d])
        index = int(input("escriba el indice de la actividad a elimiar: "))
        print(agenda[m][d][index])
        agenda[m][d][index] = None

    
run = True

while run:
    mod(accion, mes, fecha)

    z = int(input("desea realizar otra accion? 1/0: "))

    if z == 0:
        run = False
        break
    accion = int(input("¿Que deseas hacer?: "))
    mes = int(input("introduzca el mes: "))
    fecha = int(input("introduzca el dia: "))

        
print(agenda)
        
        
