import sys

a = sys.stdin.strip()
values = list(map(str, line.split()))
values = [0] + values
result = []
i = 1
n = 1
while i < (len(values) - 1):
    p = 2 ** (n - 1)
    while p < 2 ** n:
        if values[p] != '#':
            result.append(values[p])
            break
        p += 1
    i = 2 ** n
    n += 1
print('['+' '.join([i for i in result])+']')