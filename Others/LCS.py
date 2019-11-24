"""
Longest common substring

algo from wikipedia


function LCSubstr(S[1..r], T[1..n])
    L := array(1..r, 1..n)
    z := 0
    ret := {}
    for i := 1..r
        for j := 1..n
            if S[i] == T[j]
                if i == 1 or j == 1
                    L[i,j] := 1
                else
                    L[i,j] := L[i-1,j-1] + 1
                if L[i,j] > z
                    z := L[i,j]
                    ret := {S[i-z+1..z]}
                else if L[i,j] == z
                    ret := ret ∪ {S[i-z+1..z]}
            else
                L[i,j] := 0
    return ret

"""

def longestCommonSubsequence(self, text1, text2):
    """Challenge solved on leetcode
    :type text1: str
    :type text2: str
    :rtype: int
    """
    n = len(text1)
    m = len(text2)
    dp = [[0 for _ in range(m +1)] for _ in range(n+1)]
    # strings = set()
    for i in range(n):
        for j in range(m):
            if text1[i] == text2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
    return dp[n][m]



def LCSubstr(s,t):
    """
    >>> LCSubstr("ABABC","BABCA")
    BAB

    >>> LCSubstr("ABCBA","BABCA")
    ABC

    """
    r = len(s)
    n = len(t)
    L = [[0 for _ in range(n+1)] for _ in range(r+1)]
    z =  0
    ret = set()
    for i in range(0,r):
        for j in range(0,n):
            if s[i] == t[j]:
                # if i == 0 or j == 0:
                #     L[i+1][j+1] = 1
                # else:
                L[i+1][j+1] = L[i][j] + 1
                if L[i+1][j+1] > z:
                    z = L[i+1][j+1]
                    print(s[i-z +1:z])
                    ret.add(s[i-z+1:z])
                elif L[i+1][j+1] == z:
                    ret.add(s[i-z+1:z])
                    print(s[i-z +1:z])
            else:
                L[i][j] = 0
    print(ret)
    print(z)

    # for i in range(0,r):
    #     for j in range(0,n):
    #         print(L[i][j])
    return 



if __name__ == "__main__":
    import doctest
    doctest.testmod()