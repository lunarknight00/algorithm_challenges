from collections import defaultdict

graph = defaultdict(set)

def addEdge(line):
    """
    >>> addEdge("CHI:NYC:719")
    None
    >>> addEdge("NYC:LA:2414")
    3133:CHI:NYC:LA
    >>> addEdge("NYC:SEATTLE:2448")
    4862:LA:NYC:SEATTLE
    >>> addEdge("NYC:HAWAII:4924")
    7372:HAWAII:NYC:SEATTLE
    """
    depart,dest,distance = line.split(":")
    graph[depart].add((dest,int(distance)))
    graph[dest].add((depart,int(distance)))
    longestPath(graph)


def longestPath(graph):
    if len(graph) <= 2:
        return print(None)
    vertices = set(graph)
    paths = list()
    for v in vertices:
        for t in vertices:
            if v == t:
                continue
            paths.append(bfs_paths(graph,v,t))
    longest = sorted(sorted([helper(i) for i in paths],key=lambda x:x[1],reverse = True)[0:2])[0]
    return print(f"{longest[1]}:{longest[0][0]}:{longest[0][1]}:{longest[0][2]}")


# two step bfs search
def bfs_paths(graph,start,goal):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        if type(vertex) == tuple:
        	vertex = vertex[0]
        if vertex not in visited:
            visited.add(vertex)
        else:
            continue
        for next in graph[vertex] - set(path):        	
            if next[0] == goal:
                if next[0] not in visited:
                    visited.add(next[0])
                    return path + [next]
                else:
                    continue
            else:
                queue.append((next, path + [next]))

def helper(path):
    loc = [path[0]]
    dis = 0
    for i in range(1,len(path)):
        loc.append(path[i][0])
        dis += path[i][1]
    return   (tuple(loc),dis)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    