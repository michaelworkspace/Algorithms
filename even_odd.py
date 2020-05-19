"""
The following problem gives good insight into working with arrays.
Given an array of integers, reorder its entries so that the even entries appear
first. This is easy if you use O(n) space, where n is the length of the array.
However, you are required to solve it without allocating additional memory.

Example:

[5, 2, 6, 9, 4, 10, 0, 1] -> [0, 2, 6, 10, 4, 9, 1, 5]
"""


from typing import List


def even_odd(A: List[int]) -> None:
    next_even = 0
    next_odd = len(A)-1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

inputs = [5, 2, 6, 9, 4, 10, 0, 1]

print(f"Inputs before being passed to even_odd function: {inputs}")

even_odd(inputs)

print(f"Inputs after being passed to function: {inputs}")
