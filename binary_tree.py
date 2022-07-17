"""
Implementation of a Binary Tree

A binary tree is a data structure in which each note has at most two children, which are referred to as the left or
right child.

Depth of a node: the length from a node, n, to the root if the BT. The depth of the root is 0

Types of BT:
1. Complete: every node except the last is completely filled and the last levels are as far left as possible
2. Full BT: a tree in which all nodes have 2 or 0 children
"""

from stacks import Stack


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self, root):
        self.root = Node(root)

    def preorder(self, start: Node, traversal: str) -> str:

        """Root -> Left -> Right"""

        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)

        return traversal

    def inorder(self, start: Node, traversal: str) -> str:

        """ Left -> Root -> Right"""

        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += str(start.value) + "-"
            traversal = self.inorder(start.right, traversal)

        return traversal

    def postorder(self, start: Node, traversal: str) -> str:

        """ Left -> Right -> Root"""

        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += str(start.value) + "-"

        return traversal

    def level_order(self, start: Node) -> str:

        if start is None:
            return ""

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while queue.size() > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_levelOrder(self, start):

        if start is None:
            return ""

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while queue.size() > 0:
            node = queue.dequeue()

            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        return traversal

    def height(self, node):

        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size_iterative(self):

        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1

        while stack:
            node = stack.pop()

            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)

        return size

    def size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)


"""
Tree Traversal is the process of visiting (checking or updating) each node in a tree, exactly once. Trees can be 
traversed in multiple ways. Most common are: 1) In-order, 2) Pre-order, 3) Post-order
"""


# Pre-order Traversal
"""
a) check if the cur node is empty/null
b) display the data part of the root) or cur node 
c) traverse the left subtree by recursively calling the pre-order method
d) do the same as c, but with the right
"""

# In-Order
"""
a) check if cur node is empty/null
b) traverse the left subtree by recursively calling the in-order method
c) display the data part of the root (or cur node)
d) do the same as c, but with the right
"""

# Post-Order
"""
a) check if cur node is empty/null
b) traverse the left subtree by recursively calling the post-order method
c) do the same as b, but with the right
d) display the data part of the root (or cur node)
"""
