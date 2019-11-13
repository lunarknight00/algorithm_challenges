# .if there exist three collinear points in a list of points.  
# Definition for a point.
import math
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

def maxPoints(point):
    """
    >>> maxPoints([Point(-1,-1),Point(0,0),Point(1,1)])
    1
    """
    countPoint = {}
    for i in point:
        if (i.x, i.y) not in countPoint:
            countPoint[(i.x, i.y)] = 0
        countPoint[(i.x, i.y)] += 1
    if len(countPoint) == 1:
        return countPoint[(i.x, i.y)]
    solutionSet = {}
    countPointKeys = list(countPoint.keys())
    for i in range(len(countPointKeys)-1):
        for j in range(i+1, len(countPointKeys)):
            point0x, point0y = countPointKeys[i]
            point1x, point1y = countPointKeys[j]
            numerator = point1y - point0y 
            denominator = point1x - point0x 
            greatestCommonDivisor = math.gcd(abs(numerator), abs(denominator))  
            if greatestCommonDivisor != 0: 
                numerator =  numerator // greatestCommonDivisor 
                denominator =  denominator // greatestCommonDivisor 
            c = (numerator * - point0x) + point0y * denominator
            if (numerator, denominator, c) not in solutionSet:
                solutionSet[(numerator, denominator, c)] = set()      
            solutionSet[(numerator, denominator, c)].add( countPointKeys[i] )
            solutionSet[(numerator, denominator, c)].add( countPointKeys[j] )
    maxPointCount = 0
    for i in solutionSet:
        currentCount = 0
        for j in solutionSet[i]:
            currentCount += countPoint[(j[0], j[1])] 
        if maxPointCount < currentCount:
            maxPointCount = currentCount
    if maxPointCount != 0:
        return 1
    else:
        return 0
if __name__ == "__main__":
    import doctest
    doctest.testmod()