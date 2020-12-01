from typing import List


def find_product(inputs: List[int]) -> int:
    """Given a list of intergers, if the sum of two element is 2020, return it's product."""


     # This is not good solution because it is O(n^2)
#    for x in INPUTS:
#        for y in INPUTS:
#            if x + y == 2020:
#                ans = x * y
#    return ans


    # This is the optimal solution because its time complexity is O(n)
    needs = [2020 - x for x in inputs]

    for num in inputs:
        if num in needs:
            return num * (2020-num)


with open("Inputs/day01.txt") as f:
    inputs = [int(line.strip()) for line in f]
    print(find_product(inputs))

