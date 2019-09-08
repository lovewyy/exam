import math
import heapq

# 
graph = {
        "A":["B", "C"],
        "B":["A", "C", "D"],
        "C":["A", "B", "D", "E"],
        "D":["B", "C", "E", "F"],
        "E":["C", "D"],
        "F":["D"]
        }

def BFS(graph, start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    parent = {start : None}
    result = []

    while len(queue) > 0:
        v = queue.pop(-1)
        nodes = graph[v]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                parent[w] = v
                seen.add(w)
        result.append(v)
    return result, parent

print(BFS(graph, "A"))

#
graph = {
        "A":{"B":5, "C":1},
        "B":{"A":5, "C":2, "D":1},
        "C":{"A":1, "B":2, "D":4, "E":8},
        "D":{"B":1, "C":4, "E":3, "F":6},
        "E":{"C":8, "D":3},
        "F":{"D":6}
        }

def initDist(graph, start):
    distance = {}
    for i in graph:
        if i != start:
            distance[i] = math.inf
    distance[start] = 0
    return distance

def BFS2(graph, start):
    pqueue = []
    heapq.heappush(pqueue, (0, start))
    parent = {start : None}
    distance = initDist(graph, start)
    seen = set()
    
    while len(pqueue) > 0:
        pair = heapq.heappop(pqueue)
        v = pair[1]
        dist = pair[0]
        nodes = graph[v].keys()
        for w in nodes:
            if w not in seen:
                if graph[v][w] + dist < distance[w]:
                    heapq.heappush(pqueue, (graph[v][w] + dist, w))
                    seen.add(v)
                    distance[w] = graph[v][w] + dist
                    parent[w] = v 
    return parent, distance

print(BFS2(graph, "A"))
                    