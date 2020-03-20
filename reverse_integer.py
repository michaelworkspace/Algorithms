"""
Reverse the digits of an integer x.

Examples:
123 -> 321
-123 -> -321
"""


# To account for a negative x integer, abs() x and check if x if negative if so multiply it by -1
def reverse_integer_type_casting(x):
    return int(str(x)[::-1]) if x > 0 else int(str(abs(x))[::-1]) * -1


assert reverse_integer_type_casting(123) == 321
assert reverse_integer_type_casting(-123) == -321


# This has a time complexity of O(n) where n is the number if digits in the integer x
# since our while loop interate n times with constant math operations
def reverse_integer_no_casting(x):
    temp = abs(x)
    sign = 1 if x > 0 else -1
    res = 0
    while temp != 0:
        res = (res * 10) + (temp % 10)
        temp = temp // 10
    return res * sign


assert reverse_integer_no_casting(123) == 321
assert reverse_integer_no_casting(-123) == -321
