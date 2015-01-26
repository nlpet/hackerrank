#!/usr/bin/py
import re

def hackerrank_tweets(s):
  if  re.search(r'hackerrank',s,re.IGNORECASE):
    return 1
  else: return 0

    
if __name__ == '__main__':
  n = input()
  total = 0
  for i in range(n):
    total += hackerrank_tweets(raw_input().strip())
  print total
