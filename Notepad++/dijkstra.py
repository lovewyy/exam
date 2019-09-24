# 无向图
import math
import heapq
graph = {   'A':{'B':5, 'C':1},
            "B":{"A":5, 'C':2, 'D':1},
            "C":{"A":1, "B":2, "D":4, "E":8},
            "D":{"B":1, "C":4, 'E':3, "F":6},
            "E":{"C":8, "D":3},
            "F":{"D":6}}

def init_distance(graph, s):
    distance = {s : 0}
    for w in graph.keys():
        if w != s:
            distance[w] = math.inf
    return distance
    
def BFS2(gragh, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    saw = set()
    parent = {s: None}
    distance = init_distance(graph, s)
    
    while len(pqueue) > 0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        node = pair[1]
        saw.add(node)
        nodes = graph[node].keys()
        for w in nodes:
            if w not in saw:
                if dist + graph[node][w] < distance[w]:
                    heapq.heappush(pqueue, (dist + graph[node][w], w))
                    parent[w] = node
                    distance[w] = dist + graph[node][w]
    return parent, distance
parent, distance = BFS2(graph, 'E')
print(parent)
print(distance)





