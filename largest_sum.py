""" Largest Sum of an Array Algo

Take an array with positive and negative integers and find the maximum sum of a contiquous array.
"""


from typing import List


def largest_sum(arr: List[int]) -> int:
    if not arr:
        return "Need to contain atleast one integer."

    # Initilize with first element in arr
    current_sum = max_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum

print(largest_sum([5, 2, -3, 6, -2, 3]))
print(largest_sum([7, 1, 2, -1, 3, 4, 10, -12, 3, 21, -19]))

# Time: O(n)
# Space: O(1)

