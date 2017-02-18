def median(arr, n, is_sorted=False):
    if not is_sorted:
        arr = sorted(arr)
    if n % 2 == 0:
        return (arr[(n - 1) // 2] + arr[n // 2]) / 2
    else:
        return arr[n // 2]


if __name__ == '__main__':
    N = int(input().strip())
    X = list(map(int, input().strip().split(' ')))
    F = list(map(int, input().strip().split(' ')))
    S = []

    for i in range(N):
        S.extend([X[i]] * F[i])

    sorted_S = sorted(S)
    N = len(sorted_S)

    if N % 2 == 0:
        s = e = N // 2
        l = s
    else:
        s = N // 2 + 1
        e = N // 2
        l = (N - 1) // 2

    q1 = median(sorted_S[:e], l, True)
    q3 = median(sorted_S[s:], l, True)

    print('{0:0.1f}'.format(q3 - q1))
