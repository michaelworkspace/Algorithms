""" Array Pair Sum Algo Question

Given an integar array, output all the unique pairs that sum up to specific value k.

Example:
pair_sum([1, 3, 2, 2], 4]) -> (1, 3), (2, 2)
"""


from typing import List, Set


def pair_sum(A: List[int], k: int) -> Set[tuple]:
    if len(A) < 2:
        print("Not enough numbers in array")
        return

    seen = set()
    output = set()

    for num in A:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    return output

print(pair_sum([1, 3, 2, 2], 4))
print(pair_sum([5], 4))
