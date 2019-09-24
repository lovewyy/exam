# 这是计算0中最大的全1的团
n = 5
m = 5

a = [ [1, 0, 0, 1, 0],
      [1, 1, 0, 1, 1],
      [1, 0, 1, 0, 1],
      [0, 1, 1, 0, 1],
      [1, 0, 1, 0, 0]]

if len(a) == 0:
    print(0)
else:
    vis = [ [ 1 for _ in range(m)] for _ in range(n)]   # vis，标记没有被访问过的为1
    
    def DFS(i, j, vis = vis):
        if i >= 0 and j >= 0 and i < n and j < m and vis[i][j] == 1 and a[i][j] == 1:
            vis[i][j] = 0                               # 标记访问过的为0
            res = DFS(i - 1, j) + DFS(i + 1, j) + DFS(i, j - 1) + DFS(i, j + 1) + 1
            return res                                  # 递归前后左右有没有1,有就加1
        else:                                           # 啥都没有返回0
            return 0
    
    res = [0]                                           # 最小为0
    for i in range(n):
        for j in range(m):
            if vis[i][j] == 1 and a[i][j] == 1:         # 遍历没有访问过的1
                res.append(DFS(i, j, vis = vis))        # DFS
    
    print(max(res))
