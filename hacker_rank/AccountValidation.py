def AccountValidation(string):
    if not string:
        return "INVALID"
    """
    >>> AccountValidation("8BADF00D")
    'INVALID'

    >>> AccountValidation("C0FFEE1C")
    'VALID'

    """
    result = str()
    dec = str(int(string[0:-2],16))
    checker = string[-2:]
    hexDec = hex(sum(int(i) for i in dec)).split('x')[-1]
    if int(hexDec,16) == int(checker,16):
        result = "VALID"
    else:
        result = "INVALID"
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

