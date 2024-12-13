"""
Algorithms for working with graphs
"""
from math import inf


def read_incidence_matrix(filename: str) -> list[list]:
    """
    :param str filename: path to file
    :returns list[list]: the incidence matrix of a given graph
    """
    with open(filename, "r", encoding="utf-8") as f:
        graph_data = f.read().splitlines()[1:-1]
    graph_ = [g.strip(";").split("->") for g in graph_data]
    graph = [[int(edge[0].strip()), int(edge[1].strip())] for edge in graph_]

    nodes_list = []
    for edge in graph:
        for node in edge:
            if node not in nodes_list:
                nodes_list.append(node)

    incidence_matrix = []
    row_num = len(nodes_list)
    column_num = len(graph)

    for i in range(row_num):
        incidence_matrix.append([0 for i in range(column_num)])
    print(graph)

    for i in nodes_list:
        for j, node in enumerate(graph):
            if i == node[0]:
                incidence_matrix[i][j] = 1
            elif i == node[1]:
                incidence_matrix[i][j] = -1
            elif i == node[0] == node[1]:
                incidence_matrix[i][j] = 2

    return incidence_matrix


def read_adjacency_matrix(filename: str) -> list[list]:
    """
    :param str filename: path to file
    :returns list[list]: the adjacency matrix of a given graph
    """
    with open(filename, "r", encoding="utf-8") as f:
        graph_data = f.read().splitlines()[1:-1]
    graph_ = [g.strip(";").split("->") for g in graph_data]
    graph = [[int(edge[0].strip()), int(edge[1].strip())] for edge in graph_]

    nodes_list = []
    for edge in graph:
        for node in edge:
            if node not in nodes_list:
                nodes_list.append(node)

    adjacency_matrix = []
    row_num = len(nodes_list)

    for i in range(row_num):
        adjacency_matrix.append([0 for i in range(row_num)])

    for i in nodes_list:
        for j in nodes_list:
            if [i, j] in graph:
                adjacency_matrix[i][j] += 1*graph.count([i, j])

    return adjacency_matrix


def read_adjacency_dict(filename: str) -> dict[int, list[int]]:
    """
    :param str filename: path to file
    :returns dict: the adjacency dict of a given graph
    """
    with open(filename, "r", encoding="utf-8") as f:
        graph_data = f.read().splitlines()[1:-1]
    graph_ = [g.strip(";").split("->") for g in graph_data]
    graph = [[int(edge[0].strip()), int(edge[1].strip())] for edge in graph_]

    adjacency_dict = {}
    nodes_list = []
    for edge in graph:
        for node in edge:
            if node not in nodes_list:
                nodes_list.append(node)

    for node in nodes_list:
        adjacency_dict[node] = []
        for edge in graph:
            if node == edge[0]:
                if edge[1] not in adjacency_dict[node]:
                    adjacency_dict[node].append(edge[1])

    return adjacency_dict


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
    visited = set()
    queue = [start]
    traversal = []

    while queue:
        curr_node = queue.pop(0)
        if curr_node not in visited:
            traversal.append(curr_node)
            visited.add(curr_node)

            neighbor_list = []
            for neighbor in graph.get(curr_node, []):
                if neighbor not in visited:
                    neighbor_list.append(neighbor)
            queue.extend(neighbor_list)
    return traversal



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
    for i in range(size):
        for j in range(size):
            for k in range(size):
                if j == k or i == k:
                    continue
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                if i == j:
                    distance[i][j] = -1
    distance = [[-1 if (distance[i][j] == inf and i == j) else distance[i][j] for j in range(size)]
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
    distance = [[graph[i][j] if graph[i][j] != 0 else inf for j in range(len(graph))]
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
    distances = [[inf for _ in range(len(graph))] for _ in range(len(graph))]
    for vertex in graph:
        for edge in graph[vertex]:
            distances[vertex][edge] = 1
    eccentricity = get_eccentricity(distances)
    return min(eccentricity)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
