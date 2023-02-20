from math import prod
for t in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	k = 0
	product1,product2 = 1,prod(a)
	while k < n:
		product1 *= a[k]
		product2 //= a[k]
		if product1 == product2:
			break
		k += 1
	if k >= n: print(-1)
	else: print(k+1)