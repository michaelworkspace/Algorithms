"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Do not return anything. Modify nums in place.
"""


from typing import List


class Solution:
    def moveZeroes_swapping(self, nums: List[int]) -> None:
        # Element swapping approach
        i = 0
        for x in range(len(nums)):
            if nums[x] != 0:
                nums[i], nums[x] = nums[x], nums[i]
                i += 1
                

    def moveZeroes_two_pointers(self, nums: List[int]) -> None:
        # Two-pointers approach. Get count of zeros and ending index of non-zeros array.
        zeros = 0
        end_of_non_zeros_ind = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                nums[end_of_non_zeros_ind] = num
                end_of_non_zeros_ind += 1
        for _ in range(zeros):
            nums[end_of_non_zeros_ind] = 0
            end_of_non_zeros_ind += 1
