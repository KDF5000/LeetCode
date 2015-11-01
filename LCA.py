#  coding:utf-8
__author__ = 'devin'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        m = root
        while m is not None:
            if p.val <= m.val <= q.val or q.val <= m.x <= p.val:
                break
            elif p.val > m.val and q.val > m.val:
                m = m.right
            elif p.val < m.val and q.val < m.val:
                m = m.left
        return m


