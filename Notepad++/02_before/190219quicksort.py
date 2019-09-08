import numpy as np

def quickSort(x, a, b):
	if a < b:
		m = partition(x, a, b)
		quickSort(x, a, m-1)
		quickSort(x, m+1, b)
		
def partition(x, a, b):
	key = x[b]
	i = a - 1
	for j in range(a, b):
		if x[j] <= key:
			i += 1
			x[i], x[j] = x[j], x[i]
	x[i+1], x[b] = x[b], x[i+1]
	return i+1

test = np.random.randint(100, size=5)
print(test)

quickSort(test, 0, 4)
print(test)