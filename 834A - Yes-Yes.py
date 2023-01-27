
for t in range(int(input())):
	string = input()
	yes =['Y','e','s']
	if string[0] not in yes:
		print('NO')
	else:
		ans = 'YES'
		n = yes.index(string[0])
		for s in string:
			if s != yes[n]:
				ans = 'NO' 
				break
			n = n+1
			if n > len(yes)-1:
				n = 0

		print(ans)

