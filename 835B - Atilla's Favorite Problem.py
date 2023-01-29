for t in range(int(input())):
	n = input()
	s = input().upper()
	for i in range(90,64,-1):
		if chr(i) in s:
			print(ord(chr(i)) - ord('A')+1)
			break