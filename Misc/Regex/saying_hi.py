#!/usr/bin/py
import re

def saying_hi(s):
  if re.search(r'^hi\s[^d]',s,re.IGNORECASE): 
    return s
  
    
if __name__ == '__main__':
  n = input()
  for i in range(n):
    s = raw_input().strip()
    if saying_hi(s): print s
