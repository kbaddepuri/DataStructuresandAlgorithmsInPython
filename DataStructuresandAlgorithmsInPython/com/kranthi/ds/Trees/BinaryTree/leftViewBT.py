"""
Print only left view of the Binary tree

   1
   
2     3

output: 1, 2

     1
     
   2     3

4    5 6     7
                8
                
output: 1,2, 4, 8
"""

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        
class LeftViewOfBT:
    def __init__(self):
        self.root = None
        self.max_level = 0

    def getRoot(self):
        return self.root

    def leftView(self, root, level):
        if root is None:
            return
        if self.max_level < level:
            print("%d\t" %root.value)
            self.max_level = level

        self.leftView(root.left, level + 1)
        self.leftView(root.right, level + 1)

node = Node(1)
node.left = Node(10)
node.right = Node(20)
node.right.right = Node(40)
lv = LeftViewOfBT()

lv.leftView(node, 1)

            