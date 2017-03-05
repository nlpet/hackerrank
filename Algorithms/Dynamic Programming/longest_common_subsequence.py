def lcs(xs, ys):
    lx, ly = len(xs), len(ys)
    result = []
    lengths = [[0] * (ly + 1) for _ in range(lx + 1)]

    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

    while lx > 0 and ly > 0:
        if lengths[lx][ly] == lengths[lx - 1][ly]:
            lx -= 1
        elif lengths[lx][ly] == lengths[lx][ly - 1]:
            ly -= 1
        else:
            result.insert(0, xs[lx - 1])
            lx -= 1
            ly -= 1
    return ' '.join(result)


n, m = list(map(int, input().strip().split(' ')))
s1 = list(map(str, input().strip().split(' ')))
s2 = list(map(str, input().strip().split(' ')))

print(lcs(s1, s2))
