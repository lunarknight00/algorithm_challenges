from math import ceil

def findMin(arr,rows,index):  
    return min(arr[i][index] for i in range(rows))

def localMin(arr,rows,columns):
    result = [findMin(arr,rows,i) for i in range(columns)]
    if not result:
        return None
    print(result)
    return sorted(result)[:3]



if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    m = [[0.5,0.5,0.5,0.5,0.5],[.5,.1,.5,.5,.5],[.5,.5,.5,.4,.5],[.5,.5,.4,.2,.3],[0.,.5,.5,.3,.4]]
    print(localMin(m,5,5))





