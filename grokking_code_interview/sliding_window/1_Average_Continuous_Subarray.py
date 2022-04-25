from cgi import test
from typing import List

def averContSubArr(arr:List[int], k:int) -> List[float]:
    """ Given an array, find the average of all contiguous subarrays of size 'K' in it.
    Bruteforce solution

    >>> averContSubArr([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
    [2.2, 2.8, 2.4, 3.6, 2.8]
    """
    res = []
    for i in range(0,len(arr)-k+1):
        res.append(sum(arr[i:i+k])/k)
    return res

def averContSubArrOp(arr:List[int], k:int) -> List[float]:
    """ Given an array, find the average of all contiguous subarrays of size 'K' in it.
    Optimized slide window solution

    >>> averContSubArrOp([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
    [2.2, 2.8, 2.4, 3.6, 2.8]
    """
    res = []
    acc = 0
    start = 0
    for i in range(len(arr)):
        acc += arr[i]
        if i - start == k -1 :
            res.append(acc/k)
            acc -= arr[start]
            start += 1
    return res


if __name__ == "__main__":
    from doctest import testmod
    testmod()