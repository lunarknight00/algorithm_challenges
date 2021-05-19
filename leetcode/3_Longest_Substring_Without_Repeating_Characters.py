class Solution:
    """
    >>> s = Solution()
    >>> s.sliding_window("abcabcbb")
    3
    >>> s.sliding_window("bbbbbbbbb")
    1
    >>> s.sliding_window_optimized("abcabcbb")
    3
    >>> s.sliding_window_optimized("bbbbbbbbb")
    1
    """
    def sliding_window(self, s: str) -> int:
        if not s:
            return 0
        chars = [0] * 128
        l = r = 0
        res = 0
        while r < len(s):
            chars[ord(s[r])] += 1
            while chars[ord(s[r])] > 1:
                chars[ord(s[l])] -= 1
                l += 1
            res = max(r - l + 1,res)
            r += 1
        return res
    def sliding_window_optimized(self, s:str) -> int:
        res = 0 
        dt = {}
        l = 0 
        for r in range(len(s)):
            if s[r] in dt:
                l = max(dt[s[r]],l)
            dt[s[r]] =  r + 1 
            res = max(r-l+ 1,res)
        return res

if __name__ == "__main__":
    from doctest import testmod
    testmod()
    