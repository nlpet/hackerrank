#!/usr/bin/py
import re

def find_hackerrank(s):
  if  re.search(r'^hackerrank$',s):
    return 0
  elif re.search(r'^hackerrank',s):
    return 1
  elif re.search(r'hackerrank$',s):
    return 2
  else: return -1

    
if __name__ == '__main__':
  n = input()
  for i in range(n):
    print find_hackerrank(raw_input().strip())
