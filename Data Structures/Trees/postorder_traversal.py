"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end=' ')
