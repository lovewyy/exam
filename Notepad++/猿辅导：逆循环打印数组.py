import sys


我 = 3
b = 我
print(b)

line = sys.stdin.readline().strip()
values = list(map(int, line.split()))

n = values[0]
m = values[1]


a = []
for i in range(n):
    line = sys.stdin.readline().strip()
    v = list(map(int, line.split()))
    a.append(v)

res = []
while a:
    c = 0
    for b in a:
        res.append(b.pop(0))
        if not b:
            a.pop(c)
        c += 1
    if a:
        res += a.pop()
    if a:
        c = len(a)
        for b in a[::-1]:
            c -= 1
            res.append(b.pop())
            if not b:
                a.pop(c)
    if a:
        res += a.pop(0)[::-1]

for i in range(len(res)):
    print(res[i], end = ' ')
print()