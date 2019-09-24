import sys
line = sys.stdin.readline().strip()
data1 = list(map(int, line.split(',')))
n = data1[0]
m = data1[1]

data = []

for i in range(n):
    line = sys.stdin.readline().strip()
    data1 = list(map(int, line.split(',')))
    data.append(data1)

if len(data) == 0:
    print(0)
else:
    ana = [[1 for _ in range(m)] for _ in range(n)]
    
    def DFS(i, j, ana = ana):
        if i >= 0  and j >= 0 and i<n and j<m and ana[i][j] == 1 and data[i][j] == 1:
            ana[i][j] = 0
            anb = DFS(i - 1, j) + DFS(i + 1, j) + DFS(i, j - 1) + DFS(i, j + 1) + 1
            return anb
        else:
            return 0
            
    anc = [0]
    
    for i in range(n):
        for j in range(m):
            if ana[i][j] == 1 and data[i][j] == 1:
                t = DFS(i, j, ana = ana)
                anc.append(t)
    print(max(anc))