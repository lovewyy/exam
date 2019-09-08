count = 0

def perm(a, p, e):
    global count
    if p == e:
        print(a)
        count += 1
    for i in range(p, e):
        a[i], a[p] = a[p], a[i]
        perm(a, p+1, e)
        a[i], a[p] = a[p], a[i]
        
arr = [1, 2, 3, 4]
perm(arr, 0, 3)
print(count)