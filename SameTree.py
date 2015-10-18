# coding: utf-8
__author__ = 'devin'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True

        if p is not None and q is not None and p.val == q.val:
            left_tree = self.isSameTree(p.left, q.left)
            right_tree = self.isSameTree(p.right, q.right)
            if left_tree and right_tree:
                return True
            else:
                return False
        else:
            return False
