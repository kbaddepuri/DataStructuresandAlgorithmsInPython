# Python3 program to print all conflicting
# appointments in a given set of appointments

# Structure to represent an interval
class Node:
    def __init__(self):
        self.i = None
        self.max = None
        self.left = None
        self.right = None

def newNode(j):
    temp = Node()
    temp.i = j
    temp.max = j[1]
    return temp

def insert(node, i):
    root = node
    if root == None:
        return newNode(i)

    if i[0] < node.i[0]:
        root.left = insert(node.left, i)
    else:
        root.right = insert(node.right, i)

    if root.max < i[1]:
        root.max = i[1]

    return root

def doOverlap(i1, i2):
    if i1[0] < i2[1] and i1[1] > i2[0]:
        return True

    return False

def overlapSearch(node, i):
    if node == None:
        return None

    if(doOverlap(node.i, i)):
        return node.i

    if node.left != None and node.left.max >= i[0]:
        return overlapSearch(node.left, i)

    return overlapSearch(node.right, i)


def printConflicting(appt, n):
    root = None
    root = insert(root, appt[0])

    for i in range(1, n):
        res = overlapSearch(root, appt[i])

        if res != None:
            print(f"[ {appt[i][0]}, {appt[i][1]} ] conflicts with [ {res[0]}, {res[1]} ]")

        root = insert(root, appt[i])



# Driver code
if __name__ == '__main__':
    # Let us create interval tree
    # shown in above figure
    appt = [[1, 5], [3, 7],
            [2, 6], [10, 15],
            [5, 6], [4, 100]]

    n = len(appt)

    print("Following are conflicting intervals")

    printConflicting(appt, n)