n1 = int(input("ingrese un numero: "))
n2 = int(input("ingrese otro numero: "))
a = 0
b = 0
su = 0
ls=[]
if n1 < n2:
	for i in range(n1+1,n2):
		ls.append(i)
for i in range(len(ls)):
	su += ls[i]
print(f"la suma de los numeros {ls} = {su}")