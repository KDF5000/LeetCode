# coding: utf-8
__author__ = 'devin'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        node = head
        p = head.next
        node.next = None
        while p is not None:
            print p.val
            temp = p
            p = p.next
            temp.next = node
            node = temp
        return node

if __name__ == '__main__':
    head = None
    p = None
    for i in range(4):
        if head is None:
            head = ListNode(i)
            p = head
        else:
            p.next = ListNode(i)
            p = p.next
    p = head
    nodes = []
    while p is not None:
        nodes.append(p.val)
        p = p.next
    print nodes

    s = Solution()
    head = s.reverseList(head)
    p = head
    nodes = []
    while p is not None:
        nodes.append(p.val)
        p = p.next
    print nodes


