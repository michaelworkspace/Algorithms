""" is_anagram Algorithm Question


Write a function that checks whether string 1 and string 2 are is_anagrams.
"""


def is_anagram(s1: str, s2: str) -> bool:
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)

print(is_anagram('d oG', 'goD'))

