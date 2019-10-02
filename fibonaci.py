x = 0
y = 1
z = 0
print("0 1 " , end="")
while z < 20:
    z = x + y
    print(z ," ", end="")
    x = y
    y = z
print("end")
