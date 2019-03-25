class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not len(matrix):
            return matrix
        n = len(matrix)
        for i in range(n//2):
            for j in range(i,n-i-1):
                prev = matrix[i][j]
                matrix[i][j] = matrix[n -j -1][i]
                matrix[n-1-j][i] = matrix[n-i-1][n-1-j]
                matrix[n-i-1][n-1-j] = matrix[j][n-i-1]
                matrix[j][n-i-1] = prev


def priontmatrix(matrix):
    for i in range(len(matrix)):
        print(*matrix[i])

if __name__ == "__main__":
    pass
