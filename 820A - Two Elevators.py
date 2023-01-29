for t in range(int(input())):
	a,b,c = list(map(int,input().split()))
	timeA = a-1
	timeB = abs(b-c)+abs(c-1)
	if timeA == timeB:
		print(3)
	elif timeA < timeB:
		print(1)
 
	else:
		print(2)