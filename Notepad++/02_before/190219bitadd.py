def addBit(a, b):
	res = a
	xor = a^b
	forward = (a&b) << 1
	if forward != 0:
		res = addBit(xor, forward)
	else:
		res = xor
	return res

def minusBit(a, b):
	bb = ~(b-1)
	return addBit(a, bb)

print(addBit(3, 5))
print(minusBit(35, 57))

