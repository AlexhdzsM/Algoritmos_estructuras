meses = 12
dias =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
agenda = []

def llamado(mes, day):
    size = int(input("Cuantas actividades tendrá la fecha " + str(mes + 1) + "/" + str(day + 1) + ": "))
    dia = []
    for i in range (0, size):
        dia.append(input("Introduzca la actividad a realizar: "))


    month.append(dia)



for i in range(0, meses):
    month = []
    for j in range(0, dias[i]):
        llamado(i,j)
    agenda.append(month)

print(agenda)


    