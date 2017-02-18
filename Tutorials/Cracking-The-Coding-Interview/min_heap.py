from typing import List


class MinIntHeap:
    def __init__(self, capacity=10):
        self.size = 0
        self.capacity = capacity
        self.items = [None] * capacity

    def get_left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def get_right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2

    def get_parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def has_left_child(self, index: int) -> bool:
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index: int) -> bool:
        return self.get_right_child_index(index) < size

    def has_parent(self, index: int) -> bool:
        return self.get_parent_index(index) >= 0

    def ensure_extra_capacity(self) -> None:
        if self.size == self.capacity:
            self.items = self.items[:] + [None] * self.capacity
            self.capacity *= 2

    def left_child(self, index: int) -> int:
        return self.items[self.get_left_child_index(index)]

    def right_child(self, index: int) -> int:
        return self.items[self.get_right_child_index(index)]

    def parent(self, index: int) -> int:
        return self.items[self.get_parent_index(index)]

    def swap(self, indx1: int, indx2: int) -> None:
        self.items[indx1], self.items[indx2] = self.items[indx2], self.items[indx1]

    def peek(self) -> int:
        if self.size == 0:
            raise IndexError('Heap is empty')

        return self.items[0]

    def poll(self) -> int:
        if self.size == 0:
            raise IndexError('Heap is empty')

        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return item

    def add(self, item: int) -> None:
        self.ensure_extra_capacity()
        self.items[self.size] = item
        self.size += 1
        self.heapify_up()

    def heapify_up(self) -> None:
        ix = self.size - 1
        while self.has_parent(ix) and self.parent(ix) > self.items[ix]:
            self.swap(self.get_parent_index(ix), ix)
            index = self.get_parent_index(ix)

    def heapify_down(self) -> None:
        ix = 0
        while self.has_left_child(ix):
            smaller_child_index = self.get_left_child_index(ix)
            if self.has_right_child(ix) and self.right_child(ix) < self.left_child(ix):
                smaller_child_index = self.get_right_child_index(ix)

            if self.items[ix] < self.items[smaller_child_index]:
                break
            else:
                self.swap(ix, smaller_child_index)

            ix = smaller_child_index
