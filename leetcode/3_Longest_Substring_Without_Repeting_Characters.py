def lengthOfLongestSubstring(s: str) -> int:
    """
    >>> lengthOfLongestSubstring("abcabcbb")
    3 
    """
    hashMap = [0] * 128
    i = j = 0
    res = 0
    while j < len(s):
        hashMap[ord(s[j])] += 1
        while hashMap[ord(s[j])] > 1:
            hashMap[ord(s[i])] -= 1
            i += 1
        res = max(res, j-i+1)
        j += 1
    return res

if __name__ == "__main__":
    from doctetst import testmod
    testmod()