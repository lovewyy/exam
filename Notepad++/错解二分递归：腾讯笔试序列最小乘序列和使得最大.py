import sys
line0 = sys.stdin.readline().strip()
n = int(line0)
line1 = sys.stdin.readline().strip()
a = list(map(int, line1.split(' ')))

def func(a):
    if len(a) == 1:
        return a[0] ** 2
    if len(a) == 0:
        return 0
    if len(a) >= 2:
        m = a.index(min(a))
        if len(a[:m]) > 0:
            left = sum(a[:m]) * min(a[:m])
        else:
            left = 0
        if len(a[m+1:]) > 0:
            right = sum(a[m+1:]) * min(a[m+1:])
        else:
            right = 0
        whole = sum(a) * a[m]
        if left >= right and left > whole:
            func(a[:m])
        elif right > left and right > whole:
            func(a[m+1:])
        else:
            return whole

print(func(a))