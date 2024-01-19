import math
a=2
d=1
e = 2
f1 = 1
f2 = 1
while d>0.0001:
    f1 = f2
    f2= 1/math.factorial(a)
    a += 1
    e += f2
    d= f1-f2
print(e)
