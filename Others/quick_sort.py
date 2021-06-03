from typing import List


def quick_sort(arr):
    """
    >>> quick_sort([3, 6, 8, 10, 1, 2, 1])
    [1, 1, 2, 3, 6, 8, 10]
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    from doctest import testmod
    testmod()
