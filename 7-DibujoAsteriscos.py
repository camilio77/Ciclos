s = int(input("quieres crear un rectangulo(1), triangulo(2), o un hexagono(3)?\n"))
if(s == 1):
    al = int(input("ingrese el numero de asteriscos de altura: "))
    an = int(input("ingrese el numero de asteriscos de ancho: "))
    for i in range(al):
        for j in range(an):
            print("*",end= " ")
        print()
elif(s == 2):
    m = 1
    al = int(input("ingrese la altura de asteriscos del triangulo: "))
    print("*")
    for i in range(al):
        m += 1
        for j in range(m):
            print ("*", end= " ")
        print()
elif(s == 3):
    al =int(input("ingrese el tamaño del hexagono: "))
    lg = al + 2*(al-1)
    for i in range(al):
        cadena =''
        for j in range(al+2*i):
            cadena+='*'
        print(cadena.center(lg))
    for x in range(1,al):
        cadena =""
        for j in range(2,al+2*(al-x),1):
            cadena+='*'
        print(cadena.center(lg))
