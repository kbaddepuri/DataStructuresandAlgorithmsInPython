
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.headNode = None

    def push(self, value):
        # 1. create new node with provided value
        _new_node = Node(value)

        # 2. assign None to new node next
        _new_node.next = self.head

        # 3. assign new node to head
        if self.head is None:
            self.headNode = _new_node
        self.head = _new_node

    def print(self):
        _temp = self.head
        while _temp is not None:
            print("%d" % _temp.value)
            _temp = _temp.next

    def sum(self):
        count = 0
        _temp = self.head
        while _temp is not None:
            count += _temp.value
            _temp = _temp.next

        return count

    def length(self):
        _len = 0

        _temp = self.head
        while _temp is not None:
            _len += 1
            _temp = _temp.next

        return _len

    def remove(self, value):
        _temp = self.head

        # if head node itself has value, then assign None to it
        if _temp.value == value:
            self.head = _temp.next
            _temp = None
            return

            # Search for the key to be deleted and keep track of the previous node to change
        prev = None
        while _temp is not None:
            if _temp.value == value:
                break
            prev = _temp
            _temp = _temp.next

        # if key did not find, then return
        if _temp == None:
            return

            # if found then we need to delete the reference
        prev.next = _temp.next
        _temp = None

    def reverse(self):
        current = self.head
        prev = None

        while current is not None:
            _next = current.next
            current.next = prev
            prev = current
            current = _next
        self.head = prev

    def insert_after(self, existing_value, new_value):
        _head = self.head

        # create new node with new_node
        new_node = Node(new_value)

        prev = None

        # loop through all nodes and insert after that
        while _head is not None:
            if _head.value == existing_value:
                prev = _head
                break
            _head = _head.next

        if prev is None:
            print("no existing value found")
            return

        new_node.next = prev.next
        prev.next = new_node


linkedList = LinkedList()
linkedList.push(4)
linkedList.push(3)
linkedList.push(6)
linkedList.push(85)
linkedList.push(50)

print("Sum for the provide linked list is : %s " % linkedList.sum())
print("length of the provided linked list is : %s" % linkedList.length())
print("Before deleting element")
linkedList.print()
# print("Delete one element")
# linkedList.remove(85)
# print("After deleting the values")
# linkedList.print()
print("insert after 3")
linkedList.insert_after(30, 7)
linkedList.print()
# linkedList.reverse()
# print("reverse linkedlist")
# linkedList.print()
