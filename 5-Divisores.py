num = int(input("ingrese un numero: "))
i = 1
ls = []
while(i <= num):
    if((num % i) == 0):
        ls.append(i)
    i += 1
print(f"los divisores de {num} son: \n{ls}")