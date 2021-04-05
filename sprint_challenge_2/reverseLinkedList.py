# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

"""
Understand
input: [1, 2, 3, 4, 5] --> output: [5, 4, 3, 2, 1]

Plan
1. iterate thru list
2. reverse list
3. return list
"""

def reverseLinkedList(l):
    prev = None
    curr = l

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev
