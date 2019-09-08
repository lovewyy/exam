#
import sys
line0 = sys.stdin.readline().strip()
n = int(line0)
line1 = sys.stdin.readline().strip()
a = list(map(int, line1.split(' ')))

res = 0
for i in range(n):
    j = i
    while j >= 0 and a[i] <= a[j]:
        j -= 1
    k = i
    while k < n and a[i] <= a[k]:
        k += 1
    part = sum(a[j+1:k]) * a[i]
    print(a[j+1:k], a[i])
    if part > res:
        res = part
print(res)
