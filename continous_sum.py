from typing import List


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
