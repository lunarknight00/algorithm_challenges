#!/bin/python3

import os
import sys
import heapq
#
# Complete the runningMedian function below.
#
def runningMedian(a):
    #
    # Write your code here.
    #
    if not a:
        return
    result,minL,maxL = [], [], []
    for e in a:
        addnumber(minL,maxL,e)
        rebalance(minL,maxL) 
        result.append(get_median(minL,maxL))
    return result

def addnumber(minL,maxL,nb):
    if not minL and not maxL:
        heapq.heappush(maxL,-nb)
        return
    if nb >= - maxL[0]:
        heapq.heappush(minL,nb)
    else:
        heapq.heappush(maxL,-nb)

def rebalance(minL,maxL):
    if len(minL) == len(maxL) + 2:
        heapq.heappush(maxL,-heapq.heappop(minL))
    elif len(maxL) == len(minL) + 2:
        heapq.heappush(minL,-heapq.heappop(maxL))

def get_median(minL,maxL):
    result = float()
    if not minL:
        result = -maxL[0]
    elif len(minL) == len(maxL) + 1:
        result = minL[0]
    elif len(minL) + 1 == len(maxL):
        result = -maxL[0]
    elif len(maxL) == len(minL):
        result = (-maxL[0] +minL[0])/2
    return float(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
