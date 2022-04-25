from typing import List

def maxSumContigousSubArr(nums:List[int], k: int)-> int:
    """Given an array of positive numbers and a positive number 'k', find the maximum sum of any contiguous subarray of size 'k'.
    >>> maxSumContigousSubArr([2, 1, 5, 1, 3, 2], 3)
    9

    >>> maxSumContigousSubArr([2, 3, 4, 1, 5], 2)
    7
    """
    res = 0
    acc = 0
    start = 0
    for i in range(len(nums)):
        acc += nums[i]
        if i - start == k - 1:
            res = max(res, acc)
            acc -= nums[start]
            start += 1
    return res

if __name__ == "__main__":
    from doctest import testmod
    testmod()