""" Common Elements in Two Sorted Arrays

Return the common elements between two sorted arrays of integers (ascending order).

Example:
[1, 3, 4, 6, 7, 9] and [1, 2, 4, 5, 9, 10] -> [1, 4, 9]
"""


from typing import List


def common_elements(l1: List[int], l2: List[int]) -> List[int]:
    return [x for x in l1 if x in l2]


print(common_elements([1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10]))
