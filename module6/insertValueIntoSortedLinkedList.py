"""
Understand
[1, 3, 4, 6] and [5] --> [1, 3, 4, 5, 6]
[1, 3, 4, 6] and [10] --> [1, 3, 4, 6, 10]
[1, 3, 4, 6] and [0] --> [0, 1, 3, 4, 6]

Plan
Add value to the list while perseving its original sorting

"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
      # def __init__(self, x):
        # self.value = x 
        # self.next = None

def insertValueIntoSortedLinkedList(l, value):
    
    insert_node = ListNode(value)
    
    if l == None:
        return insert_node
        
    if value < l.value:
        insert_node.next = l
        return insert_node
    
    cur = l
    
    while cur.next is not None:
        if value < cur.next.value:
            insert_node.next = cur.next 
            cur.next = insert_node
            return l
            
        cur = cur.next
        
    cur.next = insert_node 
    return l
