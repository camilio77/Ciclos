for j in range(1,11):
    for i in range(1,11):
        if i * j < 10:
            print((j * i),end="  ")
        else:
            print((j * i),end=" ")
        if i==10:
            print("")