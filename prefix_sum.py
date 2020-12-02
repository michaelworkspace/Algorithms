''' Return a list of the prefix sums of a subarray.

Example: [1,2,3,4,5] -> [1,3,6,10,15]
'''


from typing import List
from itertools import accumulate

def prefix_sum_standard(arr: List[int]) -> List[int]:
    n = len(arr)
    P = [0] * n
    P[0] = arr[0]
    for i in range(1, n):
        P[i] = arr[i] + sum(arr[:i])
    return P


print(prefix_sum_standard([1,2,3,4,5]))


def prefix_sum_comprehension(arr: List[int]) -> List[int]:
    # Get the sum from the beginning of arr to i+1 because slicing is non-inclusive for end-bound
    return [sum(arr[:i+1]) for i in range(len(arr))]


print(prefix_sum_comprehension([1,2,3,4,5]))


def prefix_sum_itertools(arr: List[int]) -> List[int]:
    # Using itertools.accumulate
    return list(accumulate(arr))


print(prefix_sum_itertools([1,2,3,4,5]))
