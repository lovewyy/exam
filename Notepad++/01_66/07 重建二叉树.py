# 7
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) > 0:
            root=TreeNode(pre[0])
            rootid = tin.index(root.val)
            root.left = self.reConstructBinaryTree(pre[1:rootid + 1], tin[:rootid])
            root.right = self.reConstructBinaryTree(pre[rootid + 1:], tin[rootid + 1:])
            return root