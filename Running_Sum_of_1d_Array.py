"""
Given an array nums. We define a running sum of an array as
runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""


from typing import List


def runningSum1(A: List[int]) -> List[int]:
    ans = []
    temp = 0
    for i in range(len(A)):
        temp += A[i]
        ans.append(temp)
    return ans


def runningSum2(A: List[int]) -> List[int]:
    for i in range(1, len(A)):
                   A[i] += A[i-1]
    return A


print(runningSum1([1,2,3,4]))
print(runningSum2([1,2,3,4]))
