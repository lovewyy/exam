import sys

# 输入节点数，则边的数目等于节点数-1
n = int(sys.stdin.readline().strip())

# 用字典存成一棵树 1->2 weight=3
tree = dict()
for i in range(1, n):
    line = sys.stdin.readline().strip()
    v = list(map(int, line.split()))

    if v[0] in tree:
        tree[v[0]].update({v[1]: v[2]})
    else:
        tree.update({v[0]: {v[1]: v[2]}})

print(tree)
