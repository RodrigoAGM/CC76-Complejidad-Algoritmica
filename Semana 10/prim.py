import math
import heapq as hq

def prim(G):
    n = len(G)
    visited = [False]*n
    parents = [None]*n
    distances = [math.inf]*n
    queue=[]

    hq.heappush(queue, (0,0))
    distances[0] = 0

    while len(queue) > 0:
        _, node = hq.heappop(queue)
        if visited[node]:
            continue
        visited[node] = True

        for child, weight in G[node]:
            if not visited[child] and weight < distances[child]:
                distances[child] = weight
                parents[child] = node
                hq.heappush(queue, (weight,child))

    return parents, distances 

G= [[(1,2), (2,3), (4,6)],
    [(0,2), (4,2), (5,3)],
    [(0,3), (4,1), (3,5)],
    [(2,5), (4,5), (5,6)],
    [(0,6), (1,2), (2,1), (3,5), (5,4)],
    [(1,3), (3,6), (4,4)]]

print(prim(G))