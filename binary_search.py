""" A function to check if a number is in an array using binary seach algorithm. """


def binary_search(arr, value):
    if len(arr) == 0 or (len(arr) == 1 and arr[0] != value):
        return False

    mid = arr[len(arr) // 2]

    # Recursive approach
    if value == mid:
        return True
    if value < mid:
        return binary_search(arr[:len(arr) // 2], value)
    if value > mid:
        return binary_search(arr[len(arr) // 2 + 1:], value)
