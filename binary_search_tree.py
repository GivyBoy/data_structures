"""
Implementation of a Binary Search Tree
"""


class Node:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def insert(self, root, val):

        if self.root is None:
            self.root = Node(val)
        else:
            if val < root.val:
                if root.left is None:
                    root.left = Node(val)
                else:
                    self.insert(root.left, val)
            else:
                if root.right is None:
                    root.right = Node(val)
                else:
                    self.insert(root.right, val)
        return root


