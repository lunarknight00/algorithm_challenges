def SubSetSum(array, target):
    """
    >>> SubSetSum([1, 2, 4, 7], 13)
    True

    >>> SubSetSum([1, 2, 4, 7], 15)
    False
    """
    return _backtracking(0, 0, array, target)

def _backtracking(index, sum, array, target):
    if index == len(array): return sum == target
    if _backtracking(index + 1, sum + array[index], array, target): return True
    if _backtracking(index + 1, sum, array, target): return True
    return False



if __name__ == "__main__":
    from doctest import testmod
    testmod()