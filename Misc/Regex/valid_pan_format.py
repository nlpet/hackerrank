#!/usr/bin/py
import re

def valid_pan(s):
  match = re.search(r'[A-Z]{5}[0-9]{4}[A-Z]{1}',s)
  if match: return 'YES'
  else: return 'NO'
    
    
if __name__ == '__main__':
  n = input()
  for i in range(n):
    print valid_pan(raw_input().strip())
