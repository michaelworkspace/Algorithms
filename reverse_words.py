""" Reverse Words Algo Question

Given a sentence, reversed the words.

Example:
Original: 'I am the best'
Transformed: 'best the am I'
"""

# Pythonic
def rev(s: str) -> str:
    return ' '.join(s.split()[::-1])


print("rev:", rev("I am the best"))


# Universal Algo for all computer programming language
def rev2(s: str) -> str:
    spaces = [' ']
    words = []
    i = 0

    while i < len(s):
        if s[i] not in spaces:
            # Get the index of the begining of a word
            word_start = i

            # Continue on with incrementing the index of i until we reach a space
            while i < len(s) and s[i] not in spaces:
                i += 1

            # Append the substring to words list when we reach a space
            words.append(s[word_start:i])

        # Continue incrementing i until i < len(s) is false
        i += 1

    # Return our word list in reversed  order and join to string
    return ' '.join(reversed(words))


print("rev2:", rev2("I am the best"))
