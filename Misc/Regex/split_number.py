#!/usr/bin/py
import re

def split_number(s):
  match = re.split(r'(\d{1,3})[-\s](\d{1,3})[-\s](\d{4,10})',s)
  return 'CountryCode=%s,LocalAreaCode=%s,Number=%s' % (match[1],match[2],match[3])
    
if __name__ == '__main__':
  n = input()
  for i in range(n):
    print split_number(raw_input().strip())
