s = int(input("quieres ver la secuencia de collatz(1) de un numero o el largo de la de los numeros menores: "))
if(s == 1):
    n = int(input("ingrese un numero entero: "))
    ls = []
    while (n != 1):
        print(n,end=" ")
        if(n % 2 == 0):
            n = n / 2
        else:
            n = (n * 3) + 1
    print("1")
elif(s == 2):
    n = int(input("ingrese un numero: "))
    i = 1
    ls = []
    for i in range(1,n+1):
        print(i)
        while (i != 1):
            print("*",end="")
            if(i % 2 == 0):
                i = i / 2
            else:
                i = (i * 3) + 1
        print("*")
