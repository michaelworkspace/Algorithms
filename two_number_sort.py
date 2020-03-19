"""
Sort an array of 1's and 2's.

Example:
[2, 1, 1, 2, 1] -> [1, 1, 1, 2, 2]

Restrictions: Sorting uses O(nlogn) time complexity, but try to solve this in O(n) linear time.
"""


from typing import List


def two_number_sort(arr: List[int]) -> List[int]:
    start = 0
    end = len(arr) - 1
    while start < end:
        # Ordering of these if cases matters. This case needs to come first.
        if arr[start] == 2 and arr[end] == 1:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        if arr[start] == 1:
            start += 1
        if arr[end] == 2:
            end -= 1
    return arr


assert(two_number_sort([2, 1, 1, 2, 1]) == [1, 1, 1, 2, 2])
assert(two_number_sort([1, 2]) == [1, 2])
assert(two_number_sort([1]) == [1])
assert(two_number_sort([]) == [])
assert(two_number_sort([2, 2, 1, 1]) == [1, 1, 2, 2])
