from functools import lru_cache
class Solution:
    """
    >>> s = Solution()
    >>> s.nextGreaterElement(12)
    21
    >>> s.nextGreaterElement(101)
    110
    """
    def nextGreaterElement(self, n: int) -> int:
        num_str = [i for i in str(n)]
        length = len(num_str)
        result = []
        
        def _backtracking(arr, l, r, n):
            if l == r:
                if int("".join(arr)) > n:
                    result.append(int("".join(arr)))
                return
            for i in range(l,r):
                arr[l],arr[i] = arr[i], arr[l]
                _backtracking(arr,l+1,r,n)
                arr[l],arr[i] = arr[i], arr[l]

        _backtracking(num_str,0,length,n)
        return min(result) if result else -1

if __name__ == "__main__":
    from doctest import testmod
    testmod()
