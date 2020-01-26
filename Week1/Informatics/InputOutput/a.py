import math

a = int(input())
b = int(input())

# c = math.sqrt(math.pow(a,2) + math.pow(b,2))
c = math.hypot(a,b)

print(c)