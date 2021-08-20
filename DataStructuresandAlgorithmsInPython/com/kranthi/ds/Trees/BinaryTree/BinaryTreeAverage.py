class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def _collect(node, data, depth=0):
    if not node:
        return None

    if depth not in data:
        data[depth] = (node.value, 1)
    else:
        val, count = data[depth]
        val += node.value
        count += 1
        data[depth] = (val, count)

    _collect(node.left, data, depth + 1)
    _collect(node.right, data, depth + 1)


def avg_by_depth(node):
    data = {}
    result = []
    _collect(node, data)

    for val, count in data.items():
        result.append(val / count)

    return result
