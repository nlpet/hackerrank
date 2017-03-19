#!/bin/python3


def bubble_sort(n, a):
    is_sorted = False
    swaps = 0

    while not is_sorted:
        non_swaps = 0
        for i in range(1, n):
            if a[i - 1] > a[i]:
                a[i], a[i - 1] = a[i - 1], a[i]
                swaps += 1
            else:
                non_swaps += 1
        if non_swaps == n - 1:
            is_sorted = True
    return (swaps, a[0], a[-1])


def main():
    n = int(input().strip())
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    swaps, first, last = bubble_sort(n, a)
    print('Array is sorted in {} swaps.'.format(swaps))
    print('First Element: {}'.format(first))
    print('Last Element: {}'.format(last))


if __name__ == '__main__':
    main()
