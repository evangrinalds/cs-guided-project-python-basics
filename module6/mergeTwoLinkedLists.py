"""
Understand
l1 = [1, 2, 3] and l2 = [4, 5, 6] --> [1, 2, 3, 4, 5, 6]
Merge both linked lists into one

Plan
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def mergeTwoLinkedLists(l1, l2):
  #edge case for if its giving us empty nodes
  if l1 is None: 
    return l2
  elif l2 is None: 
    return l1
  current_A = l1
  current_B = l2
  head = None
  previous = None
  #set head
  if current_A.value < current_B.value: 
    head = current_A
    current_A = current_A.next 
    previous = head
  elif current_B.value < current_A.value: 
    head = current_B
    current_B = current_B.next
    previous = head
  else: 
    head = current_A
    current_A = current_A.next
    head.next = current_B
    current_B = current_B.next
    previous = head.next 
  while current_A is not None and current_B is not None:
    if current_A.value < current_B.value: 
      previous.next = current_A
      current_A = current_A.next
      previous = previous.next
      continue
    elif current_B.value < current_A.value: 
      previous.next = current_B
      current_B = current_B.next 
      previous = previous.next
      continue
    else: 
      previous.next = current_A
      current_A = current_A.next 
      previous = previous.next
      previous.next = current_B
      current_B = current_B.next 
      previous = previous.next
  if current_A is None and current_B is None: 
    return head
  if current_A is None: 
    previous.next = current_B
    return head
  else: 
    previous.next = current_A
    return head 
