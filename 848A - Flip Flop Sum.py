
for t in range(int(input())):
	n = int(input())
	numbers = list(map(int,input().split()))

	if n == 2:
		print(-sum(numbers))

	elif -1 not in numbers:
		print(sum(numbers)-4)

	else:
		for i in range(n):
			if i < n-1 and numbers[i] == -1 and numbers[i+1] == -1:
				numbers[i]=numbers[i+1] = 1
				break
		print(sum(numbers))
