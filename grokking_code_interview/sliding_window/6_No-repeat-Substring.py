
# TODO: worth to revisit
def noRepeatSubstr(s:str) -> int:
    """Given a string, find the length of the longest substring which has no repeating characters.
    >>> noRepeatSubstr("aabccbb")
    3
    >>> noRepeatSubstr("abbbb")
    2
    >>> noRepeatSubstr("abccde")
    3
    """
    res = 0
    visited = dict()
    start = 0
    for i in range(len(s)):
        if s[i] in visited:
            start = max(start, visited[s[i]] + 1)
        visited[s[i]] = i
        res = max(res, i - start + 1)
    return res

if __name__ == "__main__":
    from doctest import testmod
    testmod()