# I had to sort numbers in an array that appeared numerous 
# times and output them so that they only appeared 
# once: input -> [0001123333] output -> [0123]  

def removeDuplicate(string):
    """
    >>> removeDuplicate("0001123333")
    "0123"
    """
    result = str()
    cache = dict()
    for s in string:
        if s in cache:
            cache[s] += 1
        else:
            cache[s] = 1
    for s in string:
        if cache[s] == 1:
            result += s
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()