class treeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def preT(self, root):
        if root == None:
            return root
        print(root.value)
        preT(root.left)
        preT(root.right)
        
    def midT(