"""
Implementation of the sliding window technique
"""
from typing import Optional, List

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 4


def find_avg_arr(arr: list, k: int) -> list:
    total = sum(arr[:k])
    avg = []

    for i in range(len(arr) - k):

        if i == 0:
            avg.append(total / k)

        total -= arr[i]
        total += arr[i + k]

        avg.append(total / k)

    return avg


def find_max_avg(arr: list, k: int):
    total = sum(arr[:k])
    avg = total / k

    max_avg = avg

    for i in range(len(arr) - k):
        total -= arr[i]
        total += arr[k + i]

        avg = total / k

        max_avg = max(max_avg, avg)

    return max_avg


def find_max_sum(arr: list, k: int):
    total = sum(arr[:k])

    max_total = total

    for i in range(len(arr) - k):
        total -= arr[i]
        total += arr[k + i]

        max_total = max(max_total, total)

    return max_total


prices = [7, 1, 5, 3, 6, 4]


def lc_121(prices: List[int]) -> int:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
    future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """

    profit = 0

    buy = 0

    for i in range(1, len(prices)):
        if prices[buy] > prices[i]:
            buy = i
            continue

        profit = max(profit, prices[i] - prices[buy])

    return profit


print(lc_121(prices))
