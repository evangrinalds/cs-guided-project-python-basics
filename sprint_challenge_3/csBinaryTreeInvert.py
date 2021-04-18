"""
Understand
Flip the binary

Plan
1. if statement for root
2. define invert with function
3. invert
4. return 
"""


def csBinaryTreeInvert(root):
    if root:
        invert = csBinaryTreeInvert
        root.left, root.right = invert(root.right), invert(root.left)
        return root
