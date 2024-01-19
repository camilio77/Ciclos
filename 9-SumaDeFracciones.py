i = 1
j = 2
n = 2.0
ft = 0
fr = 0
print("Potencia / Fraccion / Suma")
while i < j:
    fr = 1.0/n
    n = n * 2.0
    ft = ft + fr
    print(f"{i}       {fr}       {ft}")
    i = i + 1
    j = j + 1
    if(fr <= 0.000001):
        j = 1
    
