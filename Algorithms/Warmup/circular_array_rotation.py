#!/bin/python3

import sys

n, k, q = [int(n) for n in input().strip().split(' ')]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

for a0 in range(q):
    m = int(input().strip())
    print(a[m - (k % n)])
