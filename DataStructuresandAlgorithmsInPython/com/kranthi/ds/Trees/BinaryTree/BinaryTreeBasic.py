


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


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
        if temp is None:
            return

        self.inorder(temp.left)
        print(temp.value, end=" ")
        self.inorder(temp.right)


if __name__ == "__main__":
    binarytree = BinaryTree()
    binarytree.insert(4)
    binarytree.insert(6)
    binarytree.insert(44)
    binarytree.insert(34)

    print("In order before inserting : ", end=" ")
    binarytree.inorder(binarytree.root)
    print()
    binarytree.insert(7)
    print("In order after inserting :" , end=" ")
    binarytree.inorder(binarytree.root)


"""
                4
              /   \
            6       44
          /  \
        34    7(new value)

"""



