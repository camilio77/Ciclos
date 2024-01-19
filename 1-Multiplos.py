#mostrar tabla de multiplicar
num = int(input("digite un numero: "))
i=1
print("la tabla de multiplicar de ese numero es: ")
while(i<=10):
    mult = num * i
    print(f"{num} X {i} = {mult}")
    i = i+1