n = '3141592653589793238462643383279'
for t in range(int(input())):
	num = input()
	i = 0
	while i < len(num):
		if num[i] != n[i]:
			break
		i = i+1
	print(i)

