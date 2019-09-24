b = [[691938,300406],[710196,624190],[858790,609485],[268029,225806],[200010,188664],[132599,612099],[329444,633495],[196657,757958],[628509,883388]]
s = [655988,180910]
f = [267728,840949]

def isEscapePossible(blocked, source, target):
    if len(blocked) == 0:
        return True

    m = 0
    n = 0
    mx = float('inf')
    nx = float('inf')
    
    for i in range(len(blocked)):
        if m < blocked[i][0]:
            m = blocked[i][0]
        if n < blocked[i][1]:
            n = blocked[i][1]

    for i in range(len(blocked)):
        if mx > blocked[i][0]:
            mx = blocked[i][0]
        if nx > blocked[i][1]:
            nx = blocked[i][1]

    m = max(m, source[0], target[0])
    n = max(n, source[1], target[1])

    mx = min(mx, source[0], target[0])
    nx = min(nx, source[1], target[1])

    a1 = m - mx + 1
    b1 = n - nx + 1
    
    if a1 > 2500 

    for i in blocked:
        i[0] -= mx
        i[1] -= nx
    
    source[0] -= mx
    source[1] -= nx
    
    target[0] -= mx
    target[1] -= nx

    b = [ [ 0 for i in range(b1)] for j in range(a1)]

    for i in range(len(b)):
        for j in range(len(b[0])):
            for k in blocked:
                if i == k[0] and j == k[1]:
                    b[i][j] = 1

    start = (source[0], source[1])
    fin = (target[0], target[1])

    if b[start[0]][start[1]] == 1:
        return False
    
    stack = []
    judge = set()

    judge.add(start)
    stack.append((start))

    result = []

    while len(stack) != 0:
        tail = stack.pop(-1)
        i = tail[0]
        j = tail[1]
        result.append(tail)
        if fin in result:
            return True
        for next1 in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if next1[0] >= 0 and next1[0] < len(b) and next1[1] >= 0 and next1[1] < len(b[0]) and b[next1[0]][next1[1]] != 1:
                if next1 not in judge:
                    stack.append(next1)
                    judge.add(next1)

        return False

print(isEscapePossible(b, s, f))