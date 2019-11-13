# the function here is to build a parse tree w.r.t 
# a given dictionary

def helper(s,wordDict,out):
    if len(s) == 0:
        return 
    for i in range(len(s)+1):
        prefix = s[0:i]
        if prefix in wordDict:
            out.append(prefix)
            helper(s[i:],wordDict,out)
            

def wordBreak( s, wordDict):
    """

    >>> wordBreak("leetcode",["leet", "code"])
    ['leet', 'code']

    """
    result = []
    helper(s,wordDict,result)
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()