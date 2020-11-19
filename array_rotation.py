""" Array Rotation

Given 2 arrays (assume no duplicates) is 1 array a rotation of another?
e.g. same size and elements but start index is different
Return True/False

Big O(N)

Solution:
Select an indexed position in list1 and gets it value. Find same element in list2 and
check index for index from there. If any variation then we know its not a rotation.
getting to the last item without a false means it is a rotation.
"""


from typing import List


def is_rotation(list1: List[int], list2: List[int]) -> bool:
    if len(list1) != len(list2):
        return False

    key = list1[0]
    key2 = list2.index(key)

    for i in range(len(list1)):
        # Restaging key2 index so we won't get a index out of range exception
        list2_index = (i + key2) % len(list1)
        if list1[i] != list2[list2_index]:
            return False

    return True


print(is_rotation([2, 4, 6, 8], [4, 6, 8, 2]))
