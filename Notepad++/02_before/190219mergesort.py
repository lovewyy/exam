import numpy as np

def merge(a, b):
	i = j = 0
	result = []
	m = len(a)
	n = len(b)
	while i < m and j < n:
		if a[i] <= b[j]:
			result.append(a[i])
			i += 1
		else:
			result.append(b[j])
			j += 1
	result += a[i:]
	result += b[j:]
	return result

def mergeSort(lis):
	if len(lis) <= 1:
		return lis
	mid = int(len(lis)/2)
	a = mergeSort(lis[:mid])
	b = mergeSort(lis[mid:])
	return merge(a, b)

test = [1, 3, 5, 1, 2, 5, 7, 2, 1]
test = list(np.random.randint(10, size = 10))
print(test)

test = mergeSort(test)
print(test)
