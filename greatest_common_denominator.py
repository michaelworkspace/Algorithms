""" 
Return the greatest common denominator between a and b.
"""


def gcd(a: int, b: int) -> int:
    while b != 0:
        temp = a
        a = b
        b = temp % a

    return a


assert gcd(20, 8) == 4
