"""No idea challenge solution."""
from collections import Counter


inp = """
3 2
1 5 3
3 1
5 7
"""

data = [[int(n) for n in x.split(' ')] for x in inp.strip().split('\n')]

happiness = 0

X = set(data[1])
counted_X = Counter(data[1])

A = set(data[2])
B = set(data[3])

X_A_union = A & X
X_B_union = B & X

for n in X_A_union:
    happiness += counted_X[n]

for n in X_B_union:
    happiness -= counted_X[n]

print(happiness)
