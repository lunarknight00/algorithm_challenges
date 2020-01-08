import math 

def solve(n):
    if n & 1 == 0:
        return False
    i = 3
    n_sqrt = math.sqrt(n)
    while i <= n_sqrt:
        if n % i ==0:
            # print(111111)
            return False
        i += 2
    return True

if __name__ == "__main__":
    n = int(input())
    data = set()
    a = 0 
    b = 0
    # print(solve(7))
    for i in range(1,n//2 + 1,2):
        if solve(i) and solve(n-i):
            if i == 1 or n -i == 1:
                continue
            # print(i)
            # print(n-i)
            if i < n - i:
                a = i
                b = n-i
            else:
                a = n-i
                b = i
            # print(f"({a}{b})")
            data.add((a,b))
    # print(data)
    if len(data) > 0:
        data = sorted(list(data))[-1]
        
        # print(data)
        # for n in data:
        print(data[0],end = " ")
        print(data[1])
    else:
        print(0)