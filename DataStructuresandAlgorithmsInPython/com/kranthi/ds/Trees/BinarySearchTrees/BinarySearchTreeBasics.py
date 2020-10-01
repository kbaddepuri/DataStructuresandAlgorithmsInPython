"""

Binary Search Tree is a node-based binary tree data structure which has the following properties:

The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.

                            50
                          /    \
                        40      53
                     /    \\        \
                   30      42        57
"""


class Node:
    """
    Simple Node
    """

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    """
    Basic Binary Search Tree
    """

    def __init__(self):
        self.root = None

    def get_root_node(self):
        return self.root

    def insert(self, root, node):
        if self.root is None:
            self.root = node
            return

        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                self.insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                self.insert(root.left, node)

    def inorder(self, temp):
        if not temp:
            return

        self.inorder(temp.left)
        print(temp.value, end=" ")
        self.inorder(temp.right)

    def search(self, value, temp=None):
        if temp is None:
            temp = self.root
        if temp is None or temp.value == value:
            return temp

        # if value is greater than root value
        if temp.value < value:
            self.search(value, temp.right)

        # if value is less than root value
        return self.search(value, temp.left)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(bst.get_root_node(), Node(50))
    bst.insert(bst.get_root_node(), Node(40))
    bst.insert(bst.get_root_node(), Node(53))
    bst.insert(bst.get_root_node(), Node(30))
    bst.insert(bst.get_root_node(), Node(42))
    bst.insert(bst.get_root_node(), Node(57))

    bst.inorder(bst.get_root_node())
    print(bst.search(30).value)
