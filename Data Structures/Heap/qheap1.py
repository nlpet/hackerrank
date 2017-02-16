from heapq import heappush, heappop
from sys import stdin

heap = []
lookup = set()

n = int(stdin.readline())


def add(v):
    heappush(heap, v)
    lookup.add(v)


def delete(v):
    lookup.discard(v)


def print_smallest():
    while heap[0] not in lookup:
        heappop(heap)
    print(heap[0])


mapper = {
    1: add,
    2: delete,
    3: print_smallest
}

for _ in range(n):
    q = [int(n) for n in input().strip().split(' ')]
    mapper[q[0]](*q[1:])
