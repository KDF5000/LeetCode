# coding:utf-8
__author__ = 'devin'

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p1 = node
        p2 = node.next
        while p2 is not None:
            p1.val = p2.val
            if p2.next is None:
                p1.next = None
                break
            p1 = p2
            p2 = p2.next

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    node = ListNode(1)
    p = node
    for i in range(2, 5):
        temp = ListNode(i)
        p.next = temp
        p = p.next

    p = node
    while p is not None:
        print p.val
        p = p.next

    s = Solution()
    s.deleteNode(node)
    p = node
    while p is not None:
        print p.val
        p = p.next






