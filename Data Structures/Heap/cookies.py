from heapq import heappush, heappop, nsmallest
from sys import stdin, stdout

n, k = [int(n) for n in stdin.readline().strip().split(' ')]
heap = [int(n) for n in stdin.readline().strip().split(' ')]
ops = 0
smallest = nsmallest(1, heap)[0]

while smallest < k:
    if len(heap) == 1:
        ops = -1
        break

    smallest = heappop(heap) + 2 * heappop(heap)
    heappush(heap, smallest)
    ops += 1

print(ops)
