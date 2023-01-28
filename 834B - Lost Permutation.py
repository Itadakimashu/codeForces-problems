for t in range(int(input())):
	m,s = list(map(int,input().split()))
	b = list(map(int,input().split()))
	target = sum(b)+s
	current = 0
	total = 0
	while(total < target):
		current+=1
		total += current

	ans = 'Yes'
	if total != target or max(b) > current:
		ans = 'No'
	print(ans)
