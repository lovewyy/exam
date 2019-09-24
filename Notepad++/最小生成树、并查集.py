# 最小生成树
# 并查集
import sys

# 判断一个节点的root是谁
def find(x):
    t = x
    while pre[t] != t:
        t = pre[t]
    return t

# 连通两个节点，并且是按大小顺序合并的（可以不做）
def mix(a, b):
    fa = find(a)
    fb = find(b)
    if fa != fb:
        if fa < fb:
            pre[fb] = fa
        else:
            pre[fa] = fb

# 判断两个节点是不是连通
def judge(a, b):
    fa = find(a)
    fb = find(b)
    if fa != fb:
        return False
    return True

# 判断所有节点是不是连通了
def all(n):
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if find(i) != find(j):
                return False
    return True

line = sys.stdin.readline().strip()
v = list(map(int, line.split()))

n = v[0]
m = v[1]
k = v[2]

# 存边和root
edges = []
pre = [i for i in range(n + 1)]

# 原来的直接连通
for i in range(m):
    line = sys.stdin.readline().strip()
    v = list(map(int, line.split()))
    mix(v[0], v[1])

# 添加待选的边
for i in range(k):
    line = sys.stdin.readline().strip()
    v = list(map(int, line.split()))
    edges.append((v[0], v[1], v[2]))

# 按权重排序边
def func1(edge):
    return edge[2]
edges.sort(key = func1)
print(edges)

count = 0
for item in edges:
    # 遍历待选的边，直到都连通了
    # 或者 判断所有的点都在一颗树上||边遍历完了
    if all(n) != True:
        # 待选的边的两端节点已经连通，不需要了
        if judge(item[0], item[1]) != True:
            mix(item[0], item[1])
            count += item[2]
        else:
            continue
    else:
        break 

print(count)




