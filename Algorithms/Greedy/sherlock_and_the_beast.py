#!/bin/python3

import sys

def largest_decent_number(n):
    div, rem = divmod(n, 3)
    if not div:
        return -1
    if not rem:
        return int('5' * div * 3)
    while div > 0:
        rem += 3
        div -= 1
        if rem % 5 == 0:
            return int('5' * div * 3 + '3' * rem)
    return -1
        


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_decent_number(n))
