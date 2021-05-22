'''
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.
'''
import heapq
from typing import List
def largestNumber(nums: List[int]) -> str:
    """
    >>> largestNumber([10, 2])
    '210'

    >>> largestNumber([3, 30, 34, 5, 9])
    '9534330'
    """
    pq = []
    for n in nums:
        heapq.heappush(pq,(-int((str(n)*10)[:10]),str(n)))
    res = ""
    while pq:
        res = res + heapq.heappop(pq)[1]
    return res


if __name__ == "__main__":
    from doctest import testmod
    testmod()