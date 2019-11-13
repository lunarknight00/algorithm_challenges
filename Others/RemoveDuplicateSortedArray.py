def RemoveDuplicateSortedArray(string):
    """
    >>> RemoveDuplicateSortedArray('0001123333')
    '0123'
    """
    if not string:
        return 
    return ''.join(sorted(set(string)))
        
    