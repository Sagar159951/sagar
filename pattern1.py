lst = ['A','P','Q','R']
i = 0
while i<4:
    if i>0:
        lst[i] = chr(ord(lst[i-1]) + 1)
    print(lst)
    i+=1
print('end')