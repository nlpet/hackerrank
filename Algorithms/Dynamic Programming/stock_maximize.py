#!/bin/python3


def get_max_profit(prices):
    current_max, profit = 0, 0
    for i in range(len(prices) - 1, -1, -1):
        current_max = max(current_max, prices[i])
        profit += current_max - prices[i]
    return profit


t = int(input().strip())
for a0 in range(t):
    N = int(input().strip())
    prices = list(map(int, input().strip().split(' ')))
    print(get_max_profit(prices))
