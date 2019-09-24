# 并查集

pre = [ i for i in range(n + 1)]

def find(t):
    while pre[t] != t:
        t = pre[t]
    return t

def mix(a, b):
    ra = find(a)
    rb = find(b)
    if ra != rb:
        pre[ra] = rb
        pre[a] = rb


def judge(a, b):
    if find(a) != find(b):
        return False
    return True

def all(n):
    for i in range()