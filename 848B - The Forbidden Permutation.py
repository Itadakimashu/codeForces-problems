import sys
for t in range(int(input())):
	n,m,d= list(map(int,input().split()))
	p= list(map(int,input().split()))
	a= list(map(int,input().split()))

	pos = {}
	for i in range(n):
		pos[p[i]] = i

	isGood = False
	for i in range(m-1):
		if pos[a[i]] > pos[a[i+1]] or pos[a[i+1]] > pos[a[i]]+d:
			isGood = True
			break
	if isGood:
		print(0)
	else:
		ans = sys.maxsize
		for i in range(m-1):
			ans = min(ans,pos[a[i+1]]-pos[a[i]])
		if d+1<n:
			for i in range(m-1):
				ans = min(ans,d+1-(pos[a[i+1]]-pos[a[i]])) 
		print(ans)

