from collections import Counter


def mean(arr, n):
    return sum(arr) / n


def median(arr, n):
    sorted_arr = sorted(arr)
    if n % 2 == 0:
        return (sorted_arr[(n - 1) // 2] + sorted_arr[n // 2]) / 2
    else:
        return sorted_arr[n // 2]


def mode(arr):
    ca = Counter(arr).most_common()
    max_occ = ca[0][1]
    return min(list(filter(lambda t: t[1] == max_occ, ca)), key=lambda t: t[0])[0]


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(mean(arr, n))
    print(median(arr, n))
    print(mode(arr))
