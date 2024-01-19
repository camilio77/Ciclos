#generar las potencias de 2 hasta el numero indicado
fn = int(input("ingrese hasta cual potencia de 2 ira el programa: "))
i = 0
pt = []
while(i <= 10):
    pt.append(2 ** i)
    i += 1
print(pt)