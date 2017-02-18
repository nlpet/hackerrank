import bisect


def median(arr, n):
    if n % 2 == 0:
        return (arr[(n - 1) // 2] + arr[n // 2]) / 2
    else:
        return arr[n // 2]


def add(num, arr):
    position = bisect.bisect(arr, num)
    bisect.insort(arr, num)


if __name__ == '__main__':
    N = int(input().strip())
    arr = []
    l = 0

    for _ in range(N):
        num = int(input().strip())
        add(num, arr)
        l += 1
        print('{0:.1f}'.format(median(arr, l)))
