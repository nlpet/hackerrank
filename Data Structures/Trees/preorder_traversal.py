"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def pre_order(root):
    if root:
        print(root.data, end=' ')
        pre_order(root.left)
        pre_order(root.right)
