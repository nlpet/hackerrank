import sys
data = [[int(y) for y in x.strip().split(' ')] 
                for x in sys.stdin.readlines()]

def closest_number(a, b, x):
    c = a ** b
    d = c % x
    under = int(c - d)
    over = under + x
    if c - under <= over - c:
        return under
    else:
        return over

for a, b, x in data[1:]:
    sys.stdout.write(str(closest_number(a, b, x))+'\n')
