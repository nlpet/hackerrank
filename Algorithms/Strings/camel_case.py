#!/bin/python3

import sys
from string import ascii_letters

letters = dict(zip(ascii_letters, range(52)))
s = input().strip()
words_in_s = 0

for i in range(len(s)):
    if letters[s[i]] > 25:
        words_in_s += 1

print(words_in_s + 1)
