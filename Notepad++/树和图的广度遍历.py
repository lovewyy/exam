# 树层次遍历
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def treedfs(start):
    queue = []
    queue.append(start)
    sumL = []
    while len(queue) != 0:
        sq = len(queue)
        res = 0
        for i in range(sq):
            head = queue.pop(0)
            res += head.val
            if head.left:
                queue.append(head.left)
            if head.right:
                queue.append(head.right)
        sumL.append(res)
    return sumL

n5 = Node(5, None, None)
n6 = Node(6, None, None)
n2 = Node(2, None, n5)
n3 = Node(3, n6, None)
n1 = Node(1, n2, n3)

print(treedfs(n1))

# 图的深度优先遍历
# 
graph = {
        "A":["B", "C"],
        "B":["A", "C", "D"],
        "C":["A", "B", "D", "E"],
        "D":["B", "C", "E", "F"],
        "E":["C", "D"],
        "F":["D"]
        }
        
start = "A"

def gdfs(graph, start):
    stack = []
    stack.append(start)
    res = set()
    res.add(start)
    parent = {start : None}
    
    while len(stack) != 0:                  # stack长度会变
        tail = stack.pop(-1)                # stack pop -1
        childs = graph[tail]
        for child in childs:
            if child not in res:
                stack.append(child)
                parent[child] = tail      
                res.add(child)              # 看过了
    return parent
    
print(gdfs(graph, "A"))