for t in range(int(input())):
	n = int(input())
	num = list(map(int,input()))
	ans = ''
	i = 0
	while i < n:
		if num[i] == 0:
			i = i+1
			continue
		elif i + 2 < n and num[i+2] == 0:
			if i+3 < n and num[i+3] == 0:
				ans = ans + chr(97+num[i]-1)
			else:
				ans= ans + chr(97+10*num[i] + num[i+1]-1)
				i = i+1
		else:
			ans= ans + chr(97+num[i]-1)
		i += 1
	print(ans)