class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

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

# 前序
result = []
def treeB(start):
    if start != None:
        treeB(start.left)
        result.append(tree.val)
        treeB(start.right)
    return treeB.val

# 前序，一开始就访问
def treeB2(start):
    stack = []
    result = []
    
    while start != None or len(stack) != 0:
        if start != None:
            result.append(start)
            stack.append(start)
            start = start.left
        else:
            node = stack.pop()
            start = start.right

# 中序
result = []
def treeM(start):
    if start != None:
        treeM(start.left)
        result.append(start.val)
        treeM(start.right)

treeM(n1)
print(result)

# 中序：出栈时访问
def treeM2(start):
    stack = []
    result = []
    while start != None or len(stack) != 0:
        if start != None:
            stack.append(start)
            start = start.left
        else:
            node = stack.pop()
            result.append(node.val)
            start = node.right
    return result

print(treeM2(n1))

