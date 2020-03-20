from typing import List

# Brute force solution uses O(n^3) cubic time complexity, really bad.


def maximum_array_brute_force(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    max_sum = nums[0]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            max_sum = max(max_sum, sum(nums[i:j]))
    return max_sum


# assert(maximum_array_brute_force([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)

# This approach uses a single loop with constant time operation so its time complexity is O(n).
def maximum_array(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    max_sum = nums[0]
    curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)
    return max_sum


assert(maximum_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
