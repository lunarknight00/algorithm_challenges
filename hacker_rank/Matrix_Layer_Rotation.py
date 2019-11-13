#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    if not len(matrix):
        return 
    def helper(matrix):
        m, n = len(matrix), len(matrix[0])
        # get the shape of matrix initial a start top layer 
        k, l =  0, 0
        while k < m and l < n:
            pre = matrix[k+1][m-1]
            for i in range(m-1,l-1,-1):
                curr,matrix[k][i]= matrix[k][i],pre
                pre = curr
            k += 1
            for i in range(k,m):
                curr,matrix[i][l] = matrix[i][l],pre
                pre = curr
            l += 1
            if k < m:
                for i in range(l,m):
                    curr,matrix[m-1][i] = matrix[m-1][i],pre
                    pre = curr
                m -= 1
            if l < n:
                for i in range(m-1,k-1,-1):
                    curr,matrix[i][n-1] = matrix[i][n-1],pre
                    pre = curr
                n -= 1
    for _ in range(r):
        helper(matrix)
    for i in range(len(matrix)):
        print(*matrix[i])


    

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
