# Given a 2D array, print it in spiral form. See the following examples.
# Examples:

# Input:
#         1    2   3   4
#         5    6   7   8
#         9   10  11  12
#         13  14  15  16
# Output: 
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 


# Input:
#         1   2   3   4  5   6
#         7   8   9  10  11  12
#         13  14  15 16  17  18
# Output: 
# 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11

def PrintMatrix(matrix):

    """ 
    >>> PrintMatrix([ [1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18] ])
    1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
    """
    if len(matrix) == 0:
        return
    m = len(matrix)
    n = len(matrix[0])
    k, l = 0, 0
    while k < m and l < n:
        for i in range(l,n):
            print(matrix[k][i],end = " ")
        k += 1
        for i in range(k,m):
            print(matrix[i][n-1],end =" ")
        n -= 1
        if k <m:
            for i in range(n-1,l-1,-1):
                print(matrix[m-1][i],end = " ")
            m -= 1
        if l < n:
            for i in range(m-1,k-1,-1):
                print(matrix[i][l],end = " ")
            l += 1

matrix = [ [1, 2, 3, 4, 5, 6], 
      [7, 8, 9, 10, 11, 12], 
      [13, 14, 15, 16, 17, 18] ] 
print(matrix)
PrintMatrix(matrix)

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
