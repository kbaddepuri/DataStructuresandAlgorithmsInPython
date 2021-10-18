
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Codec:
    def serialise(self, root):
        if root is None:
            return ''
        q = [root]
        sol = ''

        #run BFS
        while len(q) > 0:
            curr = q.pop(0)
            if curr is None:
                sol += '* '
                continue

            sol += str(curr.val) + ' '
            q.append(curr.left)
            q.append(curr.right)

        return sol

    def deserialise(self, data):
        if data == '':
            return None

        data_list = data.split()
        root = TreeNode(data_list[0])
        q = [root]

        idx = 1
        while len(q) > 0:
            curr = q.pop(0)
            c = data_list[idx]
            if curr == '*':
                curr.left = None
            else:
                curr.left = TreeNode(int(c))
                q.append(curr.left)

            idx += 1
            c = data_list[idx]
            if curr == '*':
                curr.right = None
            else:
                curr.right = TreeNode(int(c))
                q.append(curr.right)
        return root