# Depth First Search
# Complexity: O(V + E)


def dfs(graph, start):
    """
    It returns the set of nodes traversed in Depth First Search Order.
    """
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
