from collections import Counter

def get_input():
  N = int(raw_input().strip())
  A = [int(n) for n in raw_input().split()]
  c = Counter(A)
  return min(c,key=c.get)


def read_file():
  inp = open("input.txt").readlines()
  N = int(inp[0])
  A = [int(n) for n in inp[1].split()]
  c = Counter(A)
  return min(c,key=c.get)


print read_file()
#print get_input()
