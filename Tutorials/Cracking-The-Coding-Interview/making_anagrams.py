from math import fabs
from collections import Counter


def number_needed(a, b):
    alterations = 0
    ca, cb = Counter(a), Counter(b)
    sa, sb = set(a), set(b)
    a_b_int = sa.intersection(sb)

    for k in a_b_int:
        diff = int(fabs(ca.pop(k) - cb.pop(k)))
        alterations += diff

    alterations += sum(ca.values()) + sum(cb.values())

    return int(alterations)


a = input().strip()
b = input().strip()

print(number_needed(a, b))
