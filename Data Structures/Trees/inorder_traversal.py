"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=' ')
        in_order(root.right)
