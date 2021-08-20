'''
Program to BFS with height calulations
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.right = right
        self.left = left
        self.val = val


class BFS(object):
    def __init__(self):
        self.root = None

    def printLevelOrder(self, root):
        h = self.height(root)
        for i in range(1, h + 1):
            self.printGivenLevel(root, i)

    def printGivenLevel(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.val, end=" ")
        elif level > 1:
            self.printGivenLevel(node.left, level - 1)
            self.printGivenLevel(node.right, level - 1)

    def height(self, node):
        if node is None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1
