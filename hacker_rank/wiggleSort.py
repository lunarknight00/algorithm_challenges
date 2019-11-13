def wiggleSort(nums):
    """
    >>> wiggleSort([1, 5, 1, 1, 6, 4])
    [1, 6, 1, 5, 1, 4]
    """

    nums.sort()
    half = len(nums[::2])
    nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
    return nums
if __name__ == "__main__":
    import doctest
    doctest.testmod()