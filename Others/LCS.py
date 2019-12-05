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

def display_grid(grid):
    for i in range(len(grid)):
        print('   ', ' '.join(grid[i][j] if len(grid[i][j]) > 0 else "X" for j in range(len(grid))))


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
    # """
    # >>> LCSubstr("ABABC","BABCA")
    # BAB

    # >>> LCSubstr("ABCBA","BABCA")
    # ABC

    # """
    n = len(s)
    m = len(t)
    dp = [["" for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i+1][j +1] = dp[i][j] + s[i]
            else:
                dp[i+1][j +1] = max(dp[i+1][j],dp[i][j+1],key = lambda x:len(x))
            display_grid(dp)
            print(s[i],end = "\t")
            print(t[j])
            print(f" i,j is ({i},{j})")
            print(f"i+1,j+1 is ({i+1},{j+1})")
            print("---------------------------------------")

    return dp[n][m]




    return 



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    LCSubstr("abb","bba")