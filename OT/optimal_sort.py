#coding=utf-8
import sys
def solve(n, data):
    result = 1
    i = 0 
    paths = set()
    while i < len(data):
        m,k = data[i]
        dt = dict()

        for j in range(i +1, n):
            if data[j][1] > k:
                dt[data[j]] = j
        # print(dt)
        d = [k for k in dt]
        print(d)
        # min(d,key = lambda x:x[1])
        # foo1 = min(d,key =lambda x:x[1])
        print(min(d,key = lambda x:x[1]))
        if dt:
            pass
        i += 1
            
            

            
        

            
    pass
    
    

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    value = sys.stdin.readline().strip()
    data = list(map(int, value.split()))
    i = 0
    foo = list() 
    while i < len(data) -1:
        foo.append((data[i],data[i+1]))
        i += 2
    foo = sorted(foo)
    # print(foo)
    solve(n, foo)