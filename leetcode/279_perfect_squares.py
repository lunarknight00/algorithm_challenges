'''
leetcode 279 perfect squares

written by Henry Zhuo

'''
import math

def numSquares(n:int)-> int:
    """
    >>> numSquares(12)
    3

    >>> numSquares(13)
    2
    """
    if  <= 0:
        return 0 if n == 0 else -1
    dp = [math.inf for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,i):
            if j*j > i:
                break
            dp[i] = min(dp[i],1+dp[i-j*j])
    return dp[n]

        # if (n <= 0)
        #     return n == 0 ? 0 : -1;
        # int[] dp = new int[n + 1];
        
        # for (int i = 1; i <= n; i++) {
        #     dp[i] = Integer.MAX_VALUE;
        #     for (int j = 1; j * j <= i; j++)   
        #         dp[i] = Math.min(dp[i], 1 + dp[i - j * j]);
        # }
        
        # return dp[n];



if __name__ == "__main__":
    from doctest import testmod
    testmod()