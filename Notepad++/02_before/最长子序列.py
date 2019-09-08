import numpy as np

def findLcs(s1, s2):
    c = [ [ 0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    d = [ [ None for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                c[i+1][j+1] = c[i][j] + 1
                d[i+1][j+1] = 'ok'
            elif c[i+1][j] > c[i][j+1]:
                c[i+1][j+1] = c[i+1][j]
                d[i+1][j+1] = 'left'
            else:
                c[i+1][j+1] = c[i][j+1]
                d[i+1][j+1] = 'up'
    
    (i , j) = (len(s1), len(s2))
    
    s = []
    while c[i][j]:
        e = d[i][j]
        if e == 'ok':
            s.append(s1[i-1])
            i -= 1
            j -= 1
        if e == 'left':
            j -= 1
        if e == 'up':
            i -= 1
    s.reverse()
    return ''.join(s), c[len(s1)][len(s2)]

s1 = 'sdfdgvsdfbd'
s2 = 'dsvsbhydttysvfvfsrdfsvdfba'

print(findLcs(s1, s2))
print(findLcs(s2, s1))