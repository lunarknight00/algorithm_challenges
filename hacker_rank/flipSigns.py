def findFlips(s, k):
    """
    >>> findFlips("00011110001110", 14)
    2
    """ 
    last = '' 
    res = 0 
    for i in range(k):
        if last != s[i]: 
            res += 1
        last = s[i] 
    return res//2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
  