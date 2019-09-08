import numpy as np

print( 11 // 2 == 5)
print(11 // 2)
print(11 % 2)

def quickSort(a, l, r):
    if l < r:
        i = partition(a, l, r)
        quickSort(a, l, i-1)
        quickSort(a, i+1, r)

def partition(a, l, r):
    key = a[l]
    i = l
    for j in range(l+1, r+1):
        if a[j] < key:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i], a[l] = a[l] , a[i]
    return i

testList = list(np.random.randint(0, 100, 8))
print(testList)
quickSort(testList, 0, 7)
print(testList)

def mergeSort(a):
    lenA = len(a)
    if lenA <= 1:
        return a
    mid = lenA // 2
    l = mergeSort(a[: mid])
    r = mergeSort(a[mid:])
    return merge(l, r)

def merge(a, b):
    i = j = 0
    lenA = len(a)
    lenB = len(b)
    result = []
    while i < lenA and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:]
    result += b[j:]
    return result

testList = list(np.random.randint(0, 19, 8))
print(testList)
print(mergeSort(testList))








