"""
This file will feature some interesting array implementations
"""
from collections import defaultdict

"""
Problem 1: Given an array of non-negative integers that represents a decimal integer, add one to the integer
"""

A = [1, 4, 9]
B = [9, 9, 9, 9]

"Pythonic Implementation"


def pythonic_sol(val: list[int]) -> int:
    s = ''.join(map(str, val))
    s_add = int(s) + 1

    return s_add


"Algorithmic Implementation"


def algorithmic_implementation(val: list[int]) -> list[int]:
    val[-1] += 1
    for i in reversed(range(len(val))):
        if val[i] != 10:
            break
        val[i] = 0
        val[i - 1] += 1
        if val[0] == 10:
            val[0] = 1
            val.append(0)
    return val


"Problem 2: Two Sum (pointer method) - O(n) time and O(1) space. This assumes that the list is sorted in " \
    "ascending order"

num = [-2, 1, 2, 4, 7, 11]
t = 13


def twoSum_pointer(nums: list[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1

    while left < right:
        if (nums[left] + nums[right]) == target:
            print(nums[left], nums[right])
            return True
        elif (nums[left] + nums[right]) < target:
            left += 1
        elif (nums[left] + nums[right]) > target:
            right -= 1
    return False


"Two Sum using hash maps - O(n) time and O(n) space. Works all the time!"


def twoSum_HashMap(nums: list[int], target: int) -> bool:
    values = defaultdict(lambda: 0)
    for index, val in enumerate(nums):

        if (target - val) in values:
            print(target - val, val)
            return True
        elif target - val not in values:
            values[val] = index
    return False


"Problem 3: Assign tasks to workers so that the time it takes to complete all the tasks is minimized given a count of "\
    "workers and an array where each element indicates the duration of a task. Each worker must work on two tasks"

tasks_list = [6, 3, 2, 7, 5, 5]


def optimal_taskAssignment(tasks: list[int]) -> None:
    tasks = sorted(tasks)  # sorts the list so that the

    for i in range(len(tasks) // 2):
        print(tasks[i], tasks[~i])
        # print(i, ~i)
        # ~i the bitwise complement operator which puts a negative sign in front of i and subtracts 1 from it
        # works with even number of elements in a list, will ignore the odd element (the one that is in the middle)


"Problem 4: Intersection of two sorted arrays"

"Pythonic implementation"

list_1 = [2, 3, 3, 5, 7, 11]
list_2 = [3, 3, 7, 15, 31]

inter_list = set(list_1).intersection(list_2)


"Algorithmic Implementation"


def intersection_sortedLists(list1: list[int], list2: list[int]) -> list[int]:
    i = 0
    j = 0
    intersection = []

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            if i == 0 or list1[i] != list1[i-1]:
                intersection.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return intersection


"Problem 5: Buy and Sell a stock - look for max profit"

stock_prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


def buy_and_sell_once(prices: list[int]):
    max_profit = 0.0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit



