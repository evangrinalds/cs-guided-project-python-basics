#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def csBSTRangeSum(root, lower, upper):
    if not root: return 0
    value = root.value if lower <= root.value <= upper else 0
    return value + csBSTRangeSum(root.left, lower, upper) + csBSTRangeSum(root.right, lower, upper)
