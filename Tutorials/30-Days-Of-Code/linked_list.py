"""
Day 15: Linked List

URL: https://www.hackerrank.com/challenges/30-linked-list
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution(object):
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        if head is None:
            head = Node(data)
        else:
            current = head
            while 1:
                if current.next is None:
                    current.next = Node(data)
                    break
                current = current.next
        return head


def main():
    mylist = Solution()
    T = int(input())
    head = None
    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)
    mylist.display(head)


if __name__ == '__main__':
    main()
