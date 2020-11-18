""" Reverse Words Algo Question

Given a sentence, reversed the words.

Example:
Original: 'I am the best'
Transformed: 'best the am I'
"""

# Pythonic
def rev(s: str) -> str:
    return ' '.join(s.split()[::-1])

print(rev("I am the best"))

# Universal Algo for all computer programming language
