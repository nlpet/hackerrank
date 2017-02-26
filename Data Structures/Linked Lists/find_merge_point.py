"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
"""


def find_merge_node(head_a, head_b):
    a, b = {}, {}
    while 1:
        if head_a and head_a.data:
            aid = id(head_a.data)
            if aid in b:
                return b[aid]
            a[aid] = head_a.data
            head_a = head_a.next
        if head_b and head_b.data:
            bid = id(head_b.data)
            b[id(head_b.data)] = head_b.data
            if bid in a:
                return a[bid]
            head_b = head_b.next
