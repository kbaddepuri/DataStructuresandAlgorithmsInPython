
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, value):
        _node = Node(value)
        _node.next = self.head
        self.head = _node

    def detect_and_remove_loop(self):

        if self.head is None:
            return
        if self.head.next is None:
            return

        slow = self.head
        fast = self.head

        # move slow by one pointer and fast by two pointer
        slow = slow.next
        fast = fast.next.next

        while fast is not None:
            if fast.next is None:
                break
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next

        if slow == fast:
            slow = self.head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

            fast.next = None


