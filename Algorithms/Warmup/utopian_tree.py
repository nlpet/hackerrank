import sys

def grow(cycles):
    n = 1
    if cycles == 0: return 1
    elif cycles == 1: return 2
    else:
        if cycles % 2 == 0:
            for i in range(0,cycles-1,2):
                n = n + n + 1
            return n
        else:
            for i in range(0,cycles-1,2):
                n = n + n + 1
            return n + n


for line in sys.stdin.readlines()[1:]:
    print grow(int(line.strip()))
