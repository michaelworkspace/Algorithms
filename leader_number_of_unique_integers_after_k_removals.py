from typing import List


def foo(A: List[int], k) -> int:
    count = {}
    for num in A:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

    sfreqs = sorted(count.values())
    ans = len(sfreqs)
    
    for freq in sfreqs:
        if k >= freq:
            k -= freq
            ans -= 1
    return ans
    

print(foo([4, 3, 1, 1, 3, 3, 2], 3))
