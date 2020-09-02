"""
Given a string, find the length of the longest substring without repeating characters.

Examples:
"abcabcbb" -> "abc" -> 3
"bbbbb" -> "b" -> 1
"pwwkew" -> "kew" -> 3
"abcadcbf" -> "adcbf" -> 5

Restrictions:
Time complexity has to be O(n) linear time.
"""


def longest_substring_without_repeats(s: str) -> int:
    seen = {}
    max_len = 0
    start = 0
    for end in range(len(s)):
        if s[end] in seen:
            start = max(start, seen[s[end]]+1)
        seen[s[end]] = end
        max_len = max(max_len, end-start+1)
    return max_len


assert longest_substring_without_repeats('abcabcbb') == 3
assert longest_substring_without_repeats('bbbbb') == 1
assert longest_substring_without_repeats('pwwkew') == 3
assert longest_substring_without_repeats('abcadcbf') == 5
