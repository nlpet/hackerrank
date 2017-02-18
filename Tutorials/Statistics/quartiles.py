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
    sorted_X = sorted(X)

    q2 = int(median(sorted_X, N, True))

    if N % 2 == 0:
        s = e = N // 2
        l = s
    else:
        s = N // 2 + 1
        e = N // 2
        l = (N - 1) // 2

    q1 = int(median(sorted_X[:e], l, True))
    q3 = int(median(sorted_X[s:], l, True))

    print('{}\n{}\n{}'.format(q1, q2, q3))
