"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
"""


def FindMergeNode(headA, headB):
    a, b = {}, {}
    while 1:
        if headA and headA.data:
            aid = id(headA.data)
            if aid in b:
                return b[aid]
            a[aid] = headA.data
            headA = headA.next
        if headB and headB.data:
            bid = id(headB.data)
            b[id(headB.data)] = headB.data
            if bid in a:
                return a[bid]
            headB = headB.next
