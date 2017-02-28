from math import fabs

def get_ranks(arr):
    sorted_arr = sorted(arr)
    return [sorted_arr.index(x) + 1 for x in arr]

def get_difference_between_ranks(arr1, arr2, n):
    return [fabs(arr1[i] - arr2[i]) for i in range(n)]

def srcc(darr, n):
    return 1 - (6 * sum(map(lambda x: x ** 2, darr))) / (N * (N ** 2 - 1))


if __name__ == '__main__':
    N = int(input().strip())
    X = list(map(float, input().strip().split(' ')))
    Y = list(map(float, input().strip().split(' ')))
    ranks_x = get_ranks(X)
    ranks_y = get_ranks(Y)
    darr = get_difference_between_ranks(ranks_x, ranks_y, N)
    print('{:.3f}'.format(srcc(darr, N)))
