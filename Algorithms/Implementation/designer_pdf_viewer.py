#!/bin/python3

import sys
from string import ascii_lowercase


heights = list(map(int, input().strip().split(' ')))
word = input().strip()

letter_positions = dict(zip(ascii_lowercase, range(26)))
max_height = 0

for letter in word:
    h = heights[letter_positions[letter]]
    if h > max_height:
        max_height = h

print(max_height * len(word))
