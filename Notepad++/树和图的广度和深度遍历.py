class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def treeBfs(root):
    queue = []
    queue.append(root)
    
    result = []
    sumL = []
    
    while len(queue) != 0:
        temp = 0
        for i in range(len(queue)):
            head = queue.pop(0)
            result.append(head.val)
            temp += head.val
            if head.left != None:
                queue.append(head.left)
            if head.right != None:
                queue.append(head.right)
        sumL.append(temp)
    
    return result, sumL

def treeDfs(root):
    queue = []
    queue.append(root)
    
    result = []
    
    while len(queue) != 0:
        for i in range(len(queue)):
            head = queue.pop(-1)
            result.append(head.val)
            if head.left != None:
                queue.append(head.left)
            if head.right != None:
                queue.append(head.right)
    return result

n12 = Node(12, None, None)
n11 = Node(11, None, None)
n10 = Node(10, n12, n11)
n9 = Node(9, None, None)
n8 = Node(8, n9, None)
n7 = Node(7, None, None)
n5 = Node(5, n7, n8)
n6 = Node(6, None, n10)
n2 = Node(2, None, n5)
n3 = Node(3, n6, None)
n1 = Node(1, n2, n3)

print(treeBfs(n1))
print(treeDfs(n1))

graph = {
        "A":["B", "C"],
        "B":["A", "C", "D", "E"],
        "C":["A", "B", "E"],
        "D":["B", "E", "F"],
        "E":["B", "C", "D"],
        "F":["D"]
        }
        
start = "A"

def gBfs(graph, start):
    queue = []
    queue.append(start)
    
    parent = {start : None}
    
    judge = set()
    judge.add(start)
    
    result = []
    
    while len(queue) != 0:
        head = queue.pop(0)
        nodes = graph[head]
        result.append(head)
        for node in nodes:
            if node not in judge:
                queue.append(node)
                judge.add(node)
                parent[node] = head
    return result, parent

def gDfs(graph, start):
    queue = []
    queue.append(start)
    
    parent = {start : None}
    
    judge = set()
    judge.add(start)
    
    result = []
    
    while len(queue) != 0:
        head = queue.pop(-1)
        nodes = graph[head]
        result.append(head)
        for node in nodes:
            if node not in judge:
                queue.append(node)
                judge.add(node)
                parent[node] = head
    return result, parent

print(gBfs(graph, start))
print(gDfs(graph, start))

