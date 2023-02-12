

for t in range(int(input())):
	n = int(input())
	c = 1
	alice_bob = [0,0]
	itr = False
	while n > 0:
		alice_bob[itr] += c
		n -= c
		itr = not itr
		c += 4
	alice_bob[not itr] += n
	print(*alice_bob)




