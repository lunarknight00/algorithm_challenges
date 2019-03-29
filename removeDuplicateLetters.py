def removeDuplicate(string):
    """
    >>> removeDuplicate("cacdbebc")
    'acdbe'
    """
    result = ''
    while string:
        i = min(list(map(string.rindex,string)))
        c = min(string[:i+1])
        result += c
        string = string[string.index(c):].replace(c,'')
    return result

if __name__ == "__main__": 
    import doctest
    doctest.testmod()