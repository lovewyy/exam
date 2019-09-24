import sys

def indegree0(v, e): 
    # 如果 v 中没有顶点，返回 None
    if v == []:
        return None

    tmp = v[:]
    for i in e:
        if i[1] in tmp:
            tmp.remove(i[1])

    # 如果 v 中还有节点，但是找不到 入度=0 的
    if tmp == []:
        return -1

    # 占位删除要用的边
    for t in tmp:
        for i in range(len(e)):
            if t in e[i]:
                e[i] = 'TD' #占位，之后删掉
    if e:
        eset = set(e)
        eset.remove('TD')
        e[:] = list(eset)
    
    # 删除用过的节点
    if v:
        for t in tmp:
            v.remove(t)
    
    # 按从高到低排序
    if tmp != None:
        list(map(int, tmp)).sort()
        return list(map(str, tmp))
    else:
        return None
 
def topoSort(v, e):
    result = []
    while True:
        nodes = indegree0(v, e)
        if nodes == None:
            break
        if nodes == -1:
            # 有环
            return -1
        result.extend(nodes)
    return result

def func(a):
    return (str(a[0]), str(a[1]))

# v = list(map(str, [4, 5, 2, 3, 1]))
# e = list(map(func, [(1, 4), (2, 3), (1, 2), (1, 5), (3, 5), (4, 5)]))

v = set()
e = []

line = sys.stdin.readline().strip()
al = list(map(int, line.split()))

while al != []:
    lal = len(al)
    v.add(al[0])
    if lal != 1:
        for i in range(1, lal):
            v.add(al[i])
            e.append((al[i], al[0]))

    line = sys.stdin.readline().strip()
    al = list(map(int, line.split()))

v = list(map(str, list(v)))
e = list(map(func, e))

res = topoSort(v, e)
print(res)
