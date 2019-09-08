def lcsL(x, y):
	m = len(x)
	n = len(y)
	c = [ [ 0 for i in range(0, n+1)] for j in range(0, m+1)]
	
	for i in range(0, m+1):
		c[i][0] = 0
	for j in range(0, n+1):
		c[0][j] = 0
	for i in range(1, m+1):
		for j in range(1, n+1):
			if x[i-1] == y[j-1]:
				c[i][j] = c[i-1][j-1] + 1
			elif c[i-1][j] >= c[i][j-1]:
				c[i][j] = c[i-1][j]
			else:
				c[i][j] = c[i][j-1]
	return c

def plcs(c, x, i, j):
	if i == 0 or j == 0:
		return
	if c[i][j] == c[i-1][j]:            # equal
		plcs(c, x, i-1, j)		
	elif c[i][j] == c[i][j-1]:
		plcs(c, x, i, j-1)
	else:
		plcs(c, x, i-1, j-1)            # plcs
		print(x[i-1], end = " ")
			
c = lcsL("ABCBDAB","BDCABA" )
plcs(c, "ABCBDAB", 7, 6)

print()

x = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
y = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
c = lcsL(x, y)
plcs(c, x, len(x), len(y))