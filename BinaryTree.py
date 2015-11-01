# coding: utf-8
__author__ = 'devin'
from collections import deque

class Node:
    def __init__(self, x):
        self.va = x
        self.left = None
        self.right = Node


class BinaryTree:

    def buildTree(self, data):
        """
        :param data:List
        :return: root:TreeNode
        """
        root = None
        q = deque()

        for val in data:
            if root is None:
                root = Node(val)
                q.append(root)
            else:
                node = q.popleft()
                if node.left is None:
                    node.left = new_node
                    q.appendleft(node)
                    q.append(new_node)
                elif node.right is None:
                    new_node = Node(val)
                    node.right = new_node
                    q.append(new_node)
        return root


if __name__ == '__main__':
    data = [1, 2, 3, 4]




