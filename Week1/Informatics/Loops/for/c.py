import math

a = int(input())
b = int(input())

for number in range(a,b+1):
    j = int(math.sqrt(number))
    if j * j == number:
        print(number, end = " ")