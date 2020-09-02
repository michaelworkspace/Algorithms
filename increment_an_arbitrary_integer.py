from typing import List


""" Increment an Arbitrary-Precision Integer

Write a program which takes as input a list of digits encoded to
a non-negative decimal integer D and updates the list to
represent the integer D + 1.

For example, if the input is [1,2,9] then you should update
the list to [1,3,0].
"""


def plus_one_naive(A: List[int]) -> List[int]:
    temp = ''.join(map(str, A))
    temp = int(temp) + 1
    ans = []
    for i in str(temp):
        ans.append(int(i))
    return ans


print(plus_one_naive([1, 2, 9]))
print(plus_one_naive([1, 2, 2]))


# Time Complexity O(n)
# Space complexity O(1)
def plus_one(A: List[int]) -> List[int]:
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


print(plus_one([1, 2, 9]))
