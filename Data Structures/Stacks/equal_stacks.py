#!/bin/python3

import sys


n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

stacks = [h1, h2, h3]
sums = [sum(h1), sum(h2) ,sum(h3)]

while not (sums[0] == sums[1] == sums[2]):
    maxsum = max(sums)
    indx = sums.index(maxsum)
    sums[indx] -= stacks[indx].pop(0)

print(sums[0])
    
