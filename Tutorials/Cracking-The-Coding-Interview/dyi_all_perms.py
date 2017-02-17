from itertools import permutations


s = 'xacxzaa'
b = 'fxaazxacaaxzoecazxaxaz'


set_perms_of_s = set([''.join(p) for p in permutations(s)])
ls = len(s)

for i in range(len(b) - ls):
    substr_b = b[i:i + ls]
    if substr_b in set_perms_of_s:
        print(substr_b)
