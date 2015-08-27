from collections import Counter

def get_input():
  N = int(raw_input().strip())
  A = [int(n) for n in raw_input().split()]
  c = Counter(A)
  return min(c,key=c.get)
		
    
def read_file():
  input = open("input.txt").readlines()
  N = int(input[0])
  A = [int(n) for n in input[1].split()]
  c = Counter(A)
  return min(c,key=c.get)
  


print read_file()
#print get_input()
