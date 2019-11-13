import math
def isPowerOfTwo(n):
    if not n:
        return False
    return n and not (n&(n-1))

def solve(start,end):
    """
    >>> solve(-8,9)
    [-8, -4, -2, -1, 1, 2, 4, 8]

    >>> solve(0,9)
    [1, 2, 4, 8]
    """
    result = list()
    if start < 0:
        result = [i for i in range(start,0) if isPowerOfTwo(-i)]
        if end >= 0:
            result += [i for i in range(0,end) if isPowerOfTwo(i)]
    else:
        result = [i for i in range(start,end) if isPowerOfTwo(i)]
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()

