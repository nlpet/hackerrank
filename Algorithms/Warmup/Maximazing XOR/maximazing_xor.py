#!/bin/python


def  maxXor( l,  r):
  m = 0
  for i in range(l,r+1):
    for j in range(i,r+1):
      x = i ^ j
      if x > m: m = x
  return m

_l = int(raw_input());
_r = int(raw_input());

res = maxXor(_l, _r);
print(res)
