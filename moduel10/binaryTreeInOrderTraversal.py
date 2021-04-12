#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

"""
Understand
[2, None, 3, 4] --> [2, 4, 3]

Plan
1. recursively
"""


def binaryTreeInOrderTraversal(root):
    res = []
    helper(root, res)
    return res
    
def helper(root, res):
    if root:
        helper(root.left, res)
        res.append(root.value)
        helper(root.right, res)
