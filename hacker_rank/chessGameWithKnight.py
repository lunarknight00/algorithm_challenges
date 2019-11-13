from collections import deque

def fib(n):
	if n == 1 or n == 2:
		return 1
	return fib(n-1) + fib(n-2)

def check_boundary(r, c, n):
    return 0 <= r < n and 0 <= c < n

def bfs(a, b, n):
    q = deque([((a[0], a[1]),[a], 0)])
    dirs = [[1, 2], [-1, 2], [-1, -2], [1, -2],
            [2, 1], [-2, 1], [-2, -1], [2, -1]]
    visited = [[False]*n for _ in range(n)]
    visited[a[0]][a[1]] = True
    while q:
        tmp,path,depth = q.popleft()
        current_r, current_c = tmp
        depth += 1
        for dr, dc in dirs:
            new_r = current_r + dr
            new_c = current_c + dc
            if check_boundary(new_r, new_c, n) and not visited[new_r][new_c]:
                if new_r == b[0] and new_c == b[1]:
                    path.append((new_r,new_c))
                    return path, depth
                q.append(((new_r, new_c),path + [(new_r,new_c)], depth))
                visited[new_r][new_c] = True

    return -1

def knightL(a,b,n,checker):
    """
    >>> knightL((7,2),(0,1),8,False)
    [4, 5]

    >>> knightL( (0,0) , (1,2) , 8 , True )
    [1, 1]
    """
    if checker == False:
        white = a
        black = b
    else:
        black = a
        white = b
    path, depth = bfs(white, black, n)
    return [depth,fib(len(path))]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
