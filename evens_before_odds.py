"""
The following problem gives good insight into working with arrays.
Given an array of integers, reorder its entries so that the even entries appear
first. This is easy if you use O(n) space, where n is the length of the array.
However, you are required to solve it without allocating additional memory.
The order of the array of integers does not matter so long as the evens integers comes
before the odds.

Example:

[5, 2, 6, 9, 4, 10, 0, 1] -> [0, 2, 6, 10, 4, 9, 1, 5]
"""


from typing import List


def evens_before_odds_bruteforce(A: List[int]) -> List[int]:
    # Time complexity: O(n) linear
    # Space complexity: O(n) space where n is the size of the inputs

    evens = []
    odds = []
    for num in A:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens + odds

print(evens_before_odds_bruteforce([1,2,3,4,5,6,7,8]))


def evens_before_odds_optimal(A: List[int]) -> None:
    # Time complexity: O(n) linear
    # Space complexity: O(1) constant

    next_even = 0
    next_odd = len(A)-1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

inputs = [5, 2, 6, 9, 4, 10, 0, 1]

evens_before_odds_optimal(inputs)

print(inputs)
