import sys
str = list(sys.stdin.readline().strip())

res = []

for i in range(len(str)):
    res.append(str[i])
    if str[i] == ')':
        while len(res) != 0:
            t = res.pop(-1)
            if t == '(':
                break
    if str[i] == '<':
        if len(res) > 1 and res[-2] != '(' and res[-2] != ')' and res[-2] != '<':
            res.pop(-1)
            res.pop(-1)
        if len(res) > 1 and res[-2] == '(':
            res.pop(-1)
        if len(res) > 1 and res[-2] == ')':
            res.pop(-1)
        if len(res) > 1 and res[-2] == '<':
            res.pop(-1)
        if len(res) == 1:
            res.pop(-1)

print(''.join(res))