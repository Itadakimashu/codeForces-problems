
for t in range(int(input())):
	n = int(input())
	if n % 2 == 0:
		print(n//2,n//2)
		continue
	x = n//2
	y = n-n//2

	if n % 20 == 19:
		li_n = list(map(int,str(n)))
		li_x = []
		li_y = []
		sum_of_x = 0
		sum_of_y = 0

		for d in li_n:
			x = d//2
			y = d-d//2

			if sum_of_x >= sum_of_y:
				sum_of_x += x
				sum_of_y += y
				li_x.append(str(x))
				li_y.append(str(y))

			else:
				sum_of_x += y
				sum_of_y += x
				li_x.append(str(y))
				li_y.append(str(x))


		print(int(''.join(li_x)),int(''.join(li_y)))


	else:
		print(x,y)