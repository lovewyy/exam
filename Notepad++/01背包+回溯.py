# 01bags

def findBag(w, v, c):
    n = len(w)
    r = [ [ 0 for j in range(c+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, c+1):
            if j < w[i-1]:
                r[i][j] = r[i-1][j]
            else:
                r[i][j] = max(r[i-1][j], r[i-1][j-w[i-1]] + v[i-1])
    '''
    for i in range(n+1):
        for j in range(c+1):
            print(r[i][j], end = ' ')
        print()
    '''
    (i, j) = (n, c)
    result = []
    while i > 0 and j > 0:
        if r[i][j] == r[i-1][j]:
            i -= 1
        elif r[i][j] == r[i-1][j-w[i-1]] + v[i-1]:
            result.append(w[i-1])
            j -= w[i-1]
            i -= 1
    return r[-1][-1], result[::-1]

weight =[1, 1, 2, 3, 4, 5, 6, 7, 14]
value = [1 for i in range(len(weight))]

print(findBag(weight, value, sum(weight) // 2))