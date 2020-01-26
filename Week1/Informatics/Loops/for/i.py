import math

x = int(input())
count = 0
for n in range(1,int(math.sqrt(x+1))):
	if x % n==0:
		count+=2
if x % math.sqrt(x)==0:
	count+=1
print(count)