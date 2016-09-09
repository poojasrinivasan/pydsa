from pydsa.dfs import dfs


def test_dfs():
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}
    assert dfs(graph, 'A') == set(['E', 'D', 'F', 'A', 'C', 'B'])
