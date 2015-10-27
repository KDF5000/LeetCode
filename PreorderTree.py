# coding: utf-8
__author__ = 'devin'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        relist = []
        relist.append(root.val)
        relist.extend(self.preorderTraversal(self.preorderTraversal(root.left)))
        relist.extend(self.preorderTraversal(self.preorderTraversal(root.right)))
        return relist


    def preorderTraversal_it(self, root):
        if root is None:
            return []
        relist = []
        q = deque()
        q.appendleft(root)
        while len(q) > 0:
            node = q.popleft()
            if node is None:
                continue
            relist.append(node.val)
            q.append(node.right)
            q.append(node.left)

        return relist


