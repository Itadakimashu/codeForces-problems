for t in range(int(input())):
	n = int(input())
	string = input()
	c = [0,0]
	candy = False
	for s in string:
		if s == 'U':
			c[1] += 1
		elif s == 'D':
			c[1] -= 1
		elif s == 'R':
			c[0] += 1
		elif s == 'L':
			c[0] -= 1
		if c == [1,1]:
			candy = True
			break
	if candy:
		print('Yes')
	else:
		print('No')
