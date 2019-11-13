from math import sqrt

def dotproduct(X,Y):
    return sum(i*j for i,j in zip(X,Y))

def getDistance(X,Y):
    return sqrt((X[0] -Y[0]) **2 + (X[1] -Y[1])**2 + (X[2] -Y[2])**2)

def finIntersectionPoint(c_x,c_y,c_z,c_r,ray_x,ray_y,ray_z,dir_x,dir_y,dir_z):
    
        """
        >>> finIntersectionPoint(0.0,0.0,0.0,1.52,3.0,4.0,3.0,1.0,1.0,1.0)
        [0.0]

        """
        result = list()
        c = [c_x,c_y,c_z]
        ray = [ray_x,ray_y,ray_z]
        dir = [dir_x,dir_y,dir_z]
        L = [c[i] - ray[i] for i in range(len(c))]
        tca = dotproduct(L,dir)
        if tca < 0:
            return [0.0]
        d2 = [n - tca*tca for n in dotproduct(L,L)]
        if d2 > c_r:
            return [0.0]
        thc = sqrt(c_r-d2)
        t0 = tca - thc
        t1 = tca + thc
        if t0 == t1:
            result.append(getDistance([ray[i] + t0*dir[i] for i in range(len(ray))],ray))
        else:
            result.append(getDistance([ray[i] + t0*dir[i] for i in range(len(ray))],ray))
            result.append(getDistance([ray[i] + t1*dir[i] for i in range(len(ray))],ray))
            
if __name__ == "__main__":
    import doctest
    doctest.testmod()