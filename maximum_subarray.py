"""
Find the largest sum of a contiguous subarray (containing at least one number) within an array.

For example, given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4]
the contiguous subarray [4, -1, 2, 1] has the largest sum of 6.
"""


from typing import List


def maximum_array_brute_force(nums: List[int]) -> int:
    """
    Brute force solution uses double loops and within these nested loops our summation and slicing
    of the array each takes O(n) time bringing the total time complexity to O(n^3) cubic time. This is bad.
    """

    if len(nums) == 0:
        return 0
    max_sum = nums[0]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            max_sum = max(max_sum, sum(nums[i:j]))
    return max_sum


assert(maximum_array_brute_force([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)


def maximum_array(nums: List[int]) -> int:
    """ This approach uses a single loop with constant time operation so its time complexity is O(n). """

    if len(nums) == 0:
        return 0
    max_sum = nums[0]
    curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)
    return max_sum


assert(maximum_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
