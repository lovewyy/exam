import sys

s = sys.stdin.readline().strip()

def func(stack):
    res = []
    n = len(stack)
    t = 1
    for i in range(n):
        if stack[i] == 'L':
            t = i
            break
    count0 = 0
    count1 = 0
    for i in range(n):
        if i % 2 == 0:
            count0 += 1
        else:
            count1 += 1
    
    for i in range(n):
        if i == t and t % 2 == 0:
            res.append(count0)
        elif i == t and t % 2 == 1:
            res.append(count1)
        elif i == t - 1 and t % 2 == 1:
            res.append(count0)
        elif i == t - 1 and t % 2 == 0:
            res.append(count1)
        else:
            res.append(0)
    return res

res = []
stack = ['R']
for i in range(1, len(s)):
    if stack[-1] == 'L'and s[i] == 'R':
        res += func(stack)
        stack = []
    stack.append(s[i])
    if i == len(s) - 1:
        res += func(stack)

print(res)