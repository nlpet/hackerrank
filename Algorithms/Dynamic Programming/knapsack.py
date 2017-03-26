

def knapsack(nums, k):
    best_sum = [0] * (k + 1)
    best_sum[0] = 1

    for i, num in enumerate(nums):
        if k % nums[i] == 0 or nums[i] == 1:
            return k

    for i, num in enumerate(nums):
        for j in range(k + 1):
            if best_sum[j] and j + nums[i] <= k:
                best_sum[j + nums[i]] = 1
        if best_sum[k]:
            break

    for i in range(k, 0, -1):
        if best_sum[i]:
            return i

    return 0


def main():
    t = int(input().strip())

    for _ in range(t):
        # n = length of list, k = expected sum (not exceeding)
        n, k = list(map(int, input().strip().split(' ')))
        nums = list(map(int, input().strip().split(' ')))
        print(knapsack(nums, k))


if __name__ == '__main__':
    main()
