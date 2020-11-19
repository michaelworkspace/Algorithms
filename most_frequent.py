""" Most Frequent Algo

Given an array of numbers, what is the most frequently occurring element?
"""


from typing import List


def most_frequent(A: List[int]) -> int:
    count = {}
    max_count = 0
    max_item = 0

    for num in A:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

        if count[num] > max_count:
            max_count = count[num]
            max_item = num

    return max_item


print(most_frequent([2, 1, 2, 2, 3, 3]))
