
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class BinaryTreeBasic(object):

    def __init__(self):
        self.root = None

    def insert(self, value):
        temp = self.root
        node = Node(value)

        if self.root is None:
            self.root = node
            return

        q = []
        q.append(temp)

        while(len(q)):
            temp = q[0]
            q.pop(0)

            if not temp.left:
                temp.left = node
                break
            else:
                q.append(temp.left)

            if not temp.right:
                temp.right = node
                break
            else:
                q.append(temp.right)

    def inorder(self, temp=None):
        if not temp:
            return

        self.inorder(temp.left)
        print(temp.value, end=" ")
        self.inorder(temp.right)


if __name__ == "__main__":
    binarytree = BinaryTreeBasic()
    binarytree.insert(3)
    binarytree.insert(5)
    binarytree.insert(7)
    binarytree.insert(10)
    binarytree.insert(32)

    print("Inorder traversal before insertion : ", end=" ")
    binarytree.inorder(binarytree.root)
    binarytree.insert(90)
    print()
    print("Inorder traversal after insertion : ", end=" ")
    binarytree.inorder(binarytree.root)


    """
          3
         /  \
        5    7
       / \   /
      10  32 90        
    """