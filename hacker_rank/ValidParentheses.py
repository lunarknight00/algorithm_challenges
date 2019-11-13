def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    parentheses = {')':'(',']':'[','}':'{'}
    stack = list()
    valid = True
    index = 0
    while index < len(s) and valid:
        token = s[index]
        if token in [parentheses[k] for k in parentheses]:
            stack.append(token)
        else:
            if len(stack) == 0:
                valid = False
            else:
                top = stack.pop()
                if parentheses[token] != top:
                    valid = False
        index = index + 1
    if valid and len(stack) == 0:
        return True
    else:
        return False