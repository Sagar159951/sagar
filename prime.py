x = int(input('enter a number: '))
import math
i = 2
while i<math.sqrt(x):
    if x%i==0:
        print('number is not prime')
        break
    i+=1
else:
    print('number is prime')