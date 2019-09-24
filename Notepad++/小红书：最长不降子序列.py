import sys 

n = int(sys.stdin.readline().strip())

a = []
for i in range(n):
    line = sys.stdin.readline().strip()
    a.append(list(map(int, line.split())))

def func1(a):
    return a[1]

def func0(a):
    return a[0]

a.sort(key = func1)
print(a)
a.sort(key = func0)
print(a)

b = []
for i in range(n):
    b.append(a[i][1])

print(b)

b = [3, 2, 2, 1, 5]               # 改变了B

print(b)

dp = [1 for _ in range(len(b))]
for i in range(len(b)):
    for j in range(i):
        if b[i] >= b[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        else:
            dp[i] = dp[j]

print(dp)
print(dp[-1])

