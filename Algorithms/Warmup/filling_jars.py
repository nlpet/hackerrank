import math

def get_input():
  N,M = [int(n) for n in raw_input().split()]
  jars = [0] * N
  for i in range(M):
    a,b,k = [int(n) for n in raw_input().split()]
    for j in range(a-1,b):
      jars[j] += k
  return int(math.floor(sum(jars) / len(jars)))
		

def read_file():
  inp = open("input01.txt").readlines()
  N,M = [int(n) for n in inp[0].split()]
  jars = [0] * N

  for i in range(M):
    a,b,k = [int(n) for n in inp[1:][i].split()]
    for j in range(a-1,b):
      jars[j] += k

  return int(math.floor(sum(jars) / len(jars)))

print read_file()
print get_input()
