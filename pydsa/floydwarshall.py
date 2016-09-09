# Floyd Warshall's Algorithm
# Complexity: O(V^3)

INF = 10000


def floydwarshall(graph):
    distance = {}
    for u in graph:
        distance[u] = {}
        for v in graph:
            distance[u][v] = INF
        distance[u][u] = 0
        for neighbour in graph[u]:
            distance[u][neighbour] = graph[u][neighbour]

    for k in graph:
        for u in graph:
            for v in graph:
                distance[u][v] = min(
                    distance[u][k] + distance[k][v], distance[u][v])
    return distance
