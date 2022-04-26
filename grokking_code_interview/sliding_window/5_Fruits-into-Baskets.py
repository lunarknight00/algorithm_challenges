from typing import List
from collections import Counter

def fruitsIntoBaskets(arr: List[str]) -> int:
    """Given an array of characters where each character represents a fruit tree, 
    you are given two baskets and your goal is to put maximum number of fruits in each basket. 
    The only restriction is that each basket can have only one type of fruit.
    You can start with any tree, but once you have started you can't skip a tree. 
    You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

    >>> fruitsIntoBaskets(['A', 'B', 'C', 'A', 'C'])
    3
    >>> fruitsIntoBaskets(['A', 'B', 'C', 'B', 'B', 'C'])
    5
    """
    count = dict()
    res = 0
    start = 0
    for i in range(len(arr)):
        count.setdefault(arr[i],0)
        count[arr[i]] += 1
        while len(count) > 2:
            count[arr[start]] -= 1
            if count[arr[start]] == 0:
                count.pop(arr[start])
            start += 1
        # exit the loop, either the length of count less than 2 
        # or it is equal to 2, where we update value of res
        res = max(res, i - start + 1)
    return res

if __name__ == "__main__":
    from doctest import testmod
    testmod()