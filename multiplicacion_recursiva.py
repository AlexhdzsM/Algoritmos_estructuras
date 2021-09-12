aux = 0
def mult(num, veces):
    global aux
    aux = aux + num
    veces = veces - 1
    if veces > 0:
        mult(num, veces)
    
    return aux


print(mult(6, 5))