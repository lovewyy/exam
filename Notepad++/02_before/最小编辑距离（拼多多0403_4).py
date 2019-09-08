def minDistance(s1, s2):
    arr = [ [ 0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    
    for i in range(len(s1)+1):
        arr[i][0] = i
    for j in range(len(s2)+1):
        arr[0][j] = j

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                arr[i + 1][j + 1] = arr[i][j]
            else:
                arr[i + 1][j + 1] = min(arr[i][j + 1], arr[i + 1][j], arr[i][j]) + 1

    return arr[len(s1)][len(s2)]

print(minDistance('horse', 'ros'))
print(minDistance('intention', 'execution'))

