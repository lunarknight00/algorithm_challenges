from typing import List

def MinSubarrGivenSum(nums: List[int], s: int) -> int:
    """Given an array of positive numbers and a positive number 'S', find the length of the smallest contiguous subarray 
    whose sum is greater than or equal to 'S'. Return 0, if no such subarray exists.

    >>> MinSubarrGivenSum([2, 1, 5, 2, 3, 2], 7)
    2

    >>> MinSubarrGivenSum([2, 1, 5, 2, 8], 7)
    1

    >>> MinSubarrGivenSum([3, 4, 1, 1, 6], 8)
    3
    """
    res = float("inf")
    acc = 0
    start = 0
    for i in range(len(nums)):
        acc += nums[i]
        while acc >= s:
            res = min(res, i - start + 1)
            acc -= nums[start]
            start += 1
    return res if res != float("inf") else 0

if __name__ == "__main__":
    from doctest import testmod
    testmod()


