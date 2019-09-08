import numpy as np

def findMax(s1, s2):
    c = [ [ 0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

    m = 0
    p = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                c[i+1][j+1] = c[i][j] + 1
                if c[i+1][j+1] > m:
                    m = c[i+1][j+1]
                    p = i + 1
    return s1[p-m:p], m


s1 = "gtrnstrig"
s2 = "stringtring"
print(findMax(s1, s2))
print(findMax(s2, s1))

