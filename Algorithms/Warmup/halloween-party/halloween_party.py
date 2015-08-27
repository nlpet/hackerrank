
n = int(raw_input())

def get_pieces(k):
    if k == 1: return 0
    elif k == 2: return 1
    elif k == 3: return 2
    else:
        return (k/2) * (k/2) + ((k % 2) * (k/2))

for _ in range(n):
	print get_pieces(int(raw_input()))