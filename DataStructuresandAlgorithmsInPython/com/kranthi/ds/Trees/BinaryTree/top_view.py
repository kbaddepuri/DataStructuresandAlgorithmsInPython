"""
Print Nodes in Top View of Binary Tree
Difficulty Level : Medium
Last Updated : 04 Mar, 2021
Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. Given a binary tree, print
the top view of it. The output nodes can be printed in any order.

A node x is there in output if x is the topmost node at its horizontal distance. Horizontal distance of left child of
a node x is equal to horizontal distance of x minus 1, and that of right child is horizontal distance of x plus 1.

       1
    /     \
   2       3
  /  \    / \
 4    5  6   7
Top view of the above binary tree is
4 2 1 3 7

        1
      /   \
    2       3
      \
        4
          \
            5
             \
               6
Top view of the above binary tree is
2 1 3 6
Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
The idea is to do something similar to vertical Order Traversal. Like vertical Order Traversal,
we need to put nodes of same horizontal distance together. We do a level order traversal so that the topmost node at a
horizontal node is visited before any other node of same horizontal distance below it. Hashing is used to check if a
node at given horizontal distance is seen or not.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.hd = 0

def topView(root):
    if root is None:
        return
    q = []
    m = {}
    hd = 0
    root.hd = hd
    q.append(root)

    while len(q):
        root = q[0]
        q.pop(0)
        hd = root.hd

        if hd not in m:
            m[hd] = root.val

        if root.left:
            root.left.hd = hd - 1
            q.append(root.left)

        if root.right:
            root.right.hd = hd + 1
            q.append(root.right)

    for i in sorted(m):
        print(m[i], end=" ")


# Driver Code
if __name__ == '__main__':
    """ Create following Binary Tree
          1
        /   \
       2     3
        \
          4
           \
             5
               \
                6
    Expected output: 2 1 3 6
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)
    print("Following are nodes in top",
          "view of Binary Tree")
    topView(root)