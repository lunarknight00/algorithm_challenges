from typing import List
def insertion_sort(nums: List) -> List:
    """
    >>> insertion_sort([4, 3, 2, 1, 5])
    [1, 2, 3, 4, 5]

    >>> insertion_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]

    >>> insertion_sort([4, 3, 5, 1, 2])
    [1, 2, 3, 4, 5]
    """
    n = len(nums)
    for i in range(n-1):
        target = nums[i+1]
        j = i
        while j > -1 and nums[j] > target:
            nums[j+1], nums[j] = nums[j],nums[j+1]
            j -= 1
    return nums



if __name__ == "__main__":
    from doctest import testmod
    testmod()