"""
BFS algorithm
"""
from collections import deque


class Node(object):
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def printLevelOrder(root: Node):
    # if root is none
    if root is None:
        return

    # create an empty queue
    q = deque()

    # enque root
    q.append(root)

    while len(q) > 0:
        node = q.popleft()
        print(node.data, end=" ")

        if node.left is not None:
            q.append(node.left)

        if node.right is not None:
            q.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printLevelOrder(root)
