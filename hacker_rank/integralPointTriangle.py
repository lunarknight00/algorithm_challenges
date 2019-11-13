"""
The following solution is based on
1. find fermat point first by simulated annealing, rounded up to a integral point
2. check the point is in the triangle
"""
import math
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

def is_in_2d_polygon(point, vertices):
    angle_sum = 0
    j = 3 - 1
    for i in range(0, 3):
        sx = vertices[i].x
        sy = vertices[i].y
        tx = vertices[j].x
        ty = vertices[j].y
        k = (sy - ty) / (sx - tx + 0.000000000001)  
        b = sy - k * sx
        dis = math.fabs(k * point.x - 1 * point.y + b) / math.sqrt(k * k + 1)
        if dis < 0.000001:  
            if sx <= point.x <= tx or tx <= point.x <= sx:  
                return True
        angle = math.atan2(sy - point.y, sx - point.x) - math.atan2(ty - point.y, tx - point.x)
        if angle >= math.pi:
            angle = angle - math.pi * 2
        elif angle <= -math.pi:
            angle = angle + math.pi * 2
        angle_sum += angle
        j = i
    return math.fabs(angle_sum - math.pi * 2) < 0.00000000001
        
def getAllDistance(curr,p):
    sum = 0
    for i in range(3):
      sum += getDistance(curr,p[i])
    return sum

def getDistance(p1,p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y-p2.y)**2)

def solve(p):
    """
    >>> solve([Point(0,0),Point(1,0),Point(1,1)])
    [1, 0]
    """
    pre, cur= Point(), Point()
    dis = getAllDistance(cur,p)
    step = 10000
    r = 0.5
    direction = ((0,1),(0,-1),(-1,0),(1,0))
    node = Point()
    while step - 0.2 > 0: 
        found = True
        while found:
            found = False
            node.x = cur.x
            node.y = cur.y
            for i in range(4): 
                pre.x = direction[i][0]*step + cur.x
                pre.y = direction[i][1]*step + cur.y
                if pre.x<0 or pre.y<0:
                    continue
            tmp = getAllDistance(pre,p)
            if dis>tmp:
                dis = tmp
                node.x = pre.x
                node.y = pre.y
                found = True
            cur.x = node.x
            cur.y = node.y
        step *= r
    result = (round(node.x),round(node.y)) 
    if is_in_2d_polygon(Point(node.x,node.y), p):
        return list(result)
    else:
        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
