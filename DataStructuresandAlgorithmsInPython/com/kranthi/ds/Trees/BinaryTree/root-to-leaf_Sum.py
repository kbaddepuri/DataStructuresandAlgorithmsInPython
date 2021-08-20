class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

su = []
def rootToLeafSum(root, sm):
    if root is None:
        return

    sm += root.val
    if root.left is None and root.right is None:
        su.append(sm)
        return
    rootToLeafSum(root.left, sm)
    rootToLeafSum(root.right, sm)


node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
#node.left.right = Node(5)

rootToLeafSum(node, 0)
print(su)
