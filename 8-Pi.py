import fractions
nu = int(input("ingrese la cantidad de terminos que utilizara la suma para estimar pi: "))
pi=0
for i in range(nu):
    pi+=(-1)**(i)*(1/(2*i+1))
pi = 4 * (pi)
print(pi)