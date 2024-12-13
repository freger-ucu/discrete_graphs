"""
Algorithms for working with graphs
"""


def read_incidence_matrix(filename: str) -> list[list]:
    """
    :param str filename: path to file
    :returns list[list]: the incidence matrix of a given graph
    """
    pass


def read_adjacency_matrix(filename: str) -> list[list]:
    """
    :param str filename: path to file
    :returns list[list]: the adjacency matrix of a given graph
    """
    pass


def read_adjacency_dict(filename: str) -> dict[int, list[int]]:
    """
    :param str filename: path to file
    :returns dict: the adjacency dict of a given graph
    """
    pass


def iterative_adjacency_dict_dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    pass


def iterative_adjacency_matrix_dfs(graph: list[list], start: int) -> list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> iterative_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> iterative_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    pass


def recursive_adjacency_dict_dfs(graph: dict[int, list[int]], start: int, visited=None) -> list[int]:
    """
    Recursive dfs traversal of the graph set as a dict
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :param visited: visited vertexes for dfs traversal
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    >>> recursive_adjacency_dict_dfs({0: [2, 1], 1: [3, 2, 0], 2: [1, 0], 3: []}, 0)
    [0, 1, 2, 3]
    """
    if visited is None:
        visited = []
    visited.append(start)

    for vertex in sorted(graph[start]):
        if vertex not in visited:
            recursive_adjacency_dict_dfs(graph, vertex, visited)
    return visited


def recursive_adjacency_matrix_dfs(graph: list[list[int]], start: int, visited=None) -> list[int]:
    """
    Recursive dfs traversal of the graph set as a matrix
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :param visited: visited vertexes for dfs traversal
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> recursive_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    if visited is None:
        visited = []
    visited.append(start)

    for vertex in range(len(graph[start])):
        node = graph[start][vertex]
        if node == 1 and vertex not in visited:
            recursive_adjacency_matrix_dfs(graph, vertex, visited)
    return visited


def iterative_adjacency_dict_bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> iterative_adjacency_dict_bfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> iterative_adjacency_dict_bfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    pass


def iterative_adjacency_matrix_bfs(graph: list[list[int]], start: int) -> list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> iterative_adjacency_matrix_bfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> iterative_adjacency_matrix_bfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    pass


def get_eccentricity(distance: list[list[float]]) -> list[int]:
    """
    Implements Floyd-Warshall's algorithm to find the eccentricity of
    all vertices in a matrix and returns them as an array.
    :param list[list[float]] distance: distances matrix, where inf marks an unknown route
    :return: list[int]: the eccentricity list
    """
    size = len(distance)
    changes = 1
    while changes != 0:
        changes = 0
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    if distance[i][k] + distance[k][j] < distance[i][j]:
                        changes += 1
                        distance[i][j] = distance[i][k] + distance[k][j]
    distance = [[-1 if (distance[i][j] == float('inf') and i == j) else distance[i][j] for j in range(size)]
                for i in range(size)]
    return [max(distance[i]) for i in range(size)]


def adjacency_matrix_radius(graph: list[list]) -> int:
    """
    Uses get_eccentricity() to calculate the eccentricity of all vertices
    and returns the smallest one, which is radius by definition.
    :param list[list] graph: the adjacency matrix of a given graph
    :returns int: the radius of the graph
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    1
    >>> adjacency_matrix_radius([[0,0,1,0,0,0,0],[0,0,1,0,0,0,0],[1,1,0,1,1,0,0],\
                                [0,0,1,0,0,0,0],[0,0,1,0,0,1,0],[0,0,0,0,1,0,1],[0,0,0,0,0,1,0]])
    2
    """
    distance = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else float('inf') for j in range(len(graph))]
                for i in range(len(graph))]
    eccentricity = get_eccentricity(distance)
    return min(eccentricity)


def adjacency_dict_radius(graph: dict[int: list[int]]) -> int:
    """
    Uses get_eccentricity() to calculate the eccentricity of all vertices
    and returns the smallest one, which is radius by definition.
    :param dict graph: the adjacency list of a given graph
    :returns int: the radius of the graph
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    1
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [1]})
    2
    """
    distances = [[float('inf') if i != j else 0 for i in range(len(graph))] for j in range(len(graph))]
    for vertex in graph:
        for edge in graph[vertex]:
            if edge != vertex:
                distances[vertex][edge] = 1
    eccentricity = get_eccentricity(distances)
    return min(eccentricity)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
