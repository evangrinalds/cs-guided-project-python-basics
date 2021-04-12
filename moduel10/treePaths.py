#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

"""
Understand
["5->2->10"]

Plan
"""

def treePaths(root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.value))
            if node.right:
                stack.append((node.right, ls+str(node.value)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.value)+"->"))
        return res
