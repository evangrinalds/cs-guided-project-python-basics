#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


"""
Understand
Determine if the binary is height-balanced.
input: [5, 10, 25, None, None, 12, 3] 
output: boolean (true/false)

Plan
"""


def balancedBinaryTree(root):
        stack = [(0, root)]
        depth = {None: 0}
        while stack:
            seen, node = stack.pop()
            if node is None:
                continue
            if not seen:
                stack.extend([(1, node), (0, node.right), (0, node.left)])
            else:
                if abs(depth[node.left] - depth[node.right]) > 1:
                    return False
                depth[node] = max(depth[node.left], depth[node.right]) + 1
        return True
