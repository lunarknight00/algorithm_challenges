
from itertools import count


def longestSubstrKDisChar(s:str,k:int) -> int:
    """Given a string, find the length of the longest substring in it with no more than K distinct characters.
    
    >>> longestSubstrKDisChar("araaci", 2)
    4
    >>> longestSubstrKDisChar("araaci", 1)
    2
    >>> longestSubstrKDisChar("cbbebi", 3)
    5
    """
    res = 0
    count = {}
    start = 0
    for i in range(len(s)):
        count.setdefault(s[i],0)
        count[s[i]] += 1
        while len(count) > k:
            count[s[start]] -= 1
            if count[s[start]] == 0:
                count.pop(s[start])
            start += 1
        res = max(res, i - start + 1)
    return res

if __name__ == "__main__":
    from doctest import testmod
    testmod()