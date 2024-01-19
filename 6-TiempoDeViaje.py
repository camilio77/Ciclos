i = 2
a = 1
tt = 0
h = 0
while(i > a):
    tr = int(input("ingrese duracion del tramo: "))
    tt = tt + tr
    if(tr == 0):
        a += 2
while(tt >= 60):
    h = h + 1
    tt = tt - 60
if(tt < 10):
    str(tt)
    tt = (f"0{tt}")
print(f"el tiempo total de su viaje es de: {h}:{tt} horas")
