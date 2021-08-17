from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.peakIndexInMountainArray([0, 10, 5, 2])
        1

        >>> s.peakIndexInMountainArray([3, 4, 5, 1])
        2
        """
        begin, end  = 0, len(arr)
        res = 0
        while begin <= end:
            mid = begin + (end-begin)//2
            if mid == 0 or mid == len(arr):
                break
            if  arr[mid-1] < arr[mid] < arr[mid+1]:
                begin = mid
            elif arr[mid-1] > arr[mid] > arr[mid+1]:
                end = mid
            else:
                res = mid
                break
        return res
if __name__ == "__main__":
    from doctest import testmod
    testmod()