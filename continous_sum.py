from typing import List


# Returning a new list with the continous sums
def cont_sum(A: List[int]) -> List[int]:
    if not A:
        return None

    ans = [A[0]]
    total = A[0]
    for num in A[1:]:
        total += num
        ans.append(total)

    return ans


print(cont_sum([1,2,4,6,10]))
print(cont_sum([]))


# Returning the original Array that been modified in-placed with the continous sums
def cont_sum_inplace(A: List[int]) -> List[int]:
    for i in range(1, len(A)):
        A[i] += A[i-1]
    return A


print(cont_sum_inplace([1,2,4,6,10]))
print(cont_sum_inplace([]))
