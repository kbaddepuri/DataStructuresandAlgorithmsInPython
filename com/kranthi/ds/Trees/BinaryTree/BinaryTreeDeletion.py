
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        temp = self.root
        node = Node(value)

        if temp is None:
            self.root = node
            return

        q = []
        q.append(self.root)
        while(len(q)):
            temp = q.pop(0)

            if temp.left is None:
                temp.left = node
                break
            else:
                q.append(temp.left)
            if temp.right is None:
                temp.right = node
                break
            else:
                q.append(temp.right)

    def inorder(self, temp):
        if temp is None:
            return
        self.inorder(temp.left)
        print(temp.value, end=" ")
        self.inorder(temp.right)


    def delete_deepest(self, deep_node):
        q = []
        q.append(self.root)

        while(len(q)):
            temp = q.pop(0)
            if temp is deep_node:
                temp = None
                return

            if temp.left:
                if temp.left is deep_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)

            if temp.right:
                if temp.right is deep_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)


    def delete(self, value):
        """
            Rules to delete value:
                1. Traverse till the node found
                2. Replace found node with deepest right node
                3. Remove deepest right node ( if deepest node is None at right, get deepest left node from right
        """
        if self.root is None:
            return None
        if self.root.left is None and self.root.right is None:
            if self.root.value == value:
                return None
            return self.root

        q = []
        q.append(self.root)
        value_node = None
        temp = None
        while(len(q)):
            temp = q.pop(0)
            if temp.value == value:
                value_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

        if value_node:
            x = temp.value
            self.delete_deepest(temp)
            value_node.value = x


if __name__ == "__main__":
    binaryTree = BinaryTree()
    binaryTree.insert(4)
    binaryTree.insert(6)
    binaryTree.insert(89)
    binaryTree.insert(46)
    binaryTree.insert(56)

    print("Traversing tree before inserting a new value : ")
    binaryTree.inorder(binaryTree.root)
    print()
    print("Traversing tree after inserting a new value : ")
    binaryTree.insert(30)
    binaryTree.inorder(binaryTree.root)
    #delete 6 and 30 should replace 6 node
    binaryTree.delete(6)
    print("Traversing tree after deleting a new value : ")
    binaryTree.inorder(binaryTree.root)

"""

inorder output before deleting: 46 6 56 4 30 89
          4                                                4               inorder output after deleting: 46 30 56 4 89
        /   \                                            /   \
      6       89  ------> after deleting 6 --->        30      89
    /   \    /                                       /    \
  46     56 30                                      46      56

"""
