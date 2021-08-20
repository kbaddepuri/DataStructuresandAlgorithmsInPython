"""
you are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
 and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry_sum = 0
        carry = 0
        head = ListNode(0)
        temphead = head
        while l1  or l2  or carry:
            carry_sum = carry
            if l1:
                carry_sum += l1.val
                l1 = l1.next

            if l2:
                carry_sum += l2.val
                l2 = l2.next

            if carry_sum >= 10:
                carry_sum -= 10
                carry = 1
            else:
                carry = 0

            temphead.next = ListNode(carry_sum)
            temphead = temphead.next

        return head.next


