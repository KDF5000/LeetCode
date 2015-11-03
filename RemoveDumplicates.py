# coding: utf-8
__author__ = 'devin'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        p = head
        current_val = head.val
        while p is not None:
            # 重复就删除
            if p.next is not None and p.next.val == current_val:
                p.next = p.next.next
            else: # 没有删除节点 向后移
                if p.next is not None:
                    current_val = p.next.val
                p = p.next
        return head


if __name__ == '__main__':
    head = None
    p = None
    for i in [1,1,2,2]:
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
    head = s.deleteDuplicates(head)
    p = head
    nodes = []
    while p is not None:
        nodes.append(p.val)
        p = p.next
    print nodes



