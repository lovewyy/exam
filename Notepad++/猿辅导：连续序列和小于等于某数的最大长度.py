import sys

line = sys.stdin.readline().strip()
values = list(map(int, line.split()))

n = values[0]
m = values[1]

line = sys.stdin.readline().strip()
v = list(map(int, line.split()))

count = 0
cut = 0
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += v[j]
        if temp <= m:
            if j - i + 1 > count:
                count = j - i + 1
        else:
            break
print(count)