"""
Lab 2 template
"""

def read_incidence_matrix(filename: str) -> list[list]:
    """
    :param str filename: path to file
    :returns list[list]: the incidence matrix of a given graph
    """
    edges = []

    with open(filename, 'r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            line = line.strip().replace(';', '').replace('->', '').split()
            if len(line) == 2:
                vertex, directional_point = line
                edges.append((int(vertex), int(directional_point)))

    vertices = sorted(set(v for edge in edges for v in edge))
    num_vertices = len(vertices)
    num_edges = len(edges)

    incidence_matrix = [[0] * num_edges for _ in range(num_vertices)]

    for edge_index, (start, end) in enumerate(edges):
        incidence_matrix[start][edge_index] = 1
        incidence_matrix[end][edge_index] = -1

    return incidence_matrix

def read_adjacency_matrix(filename: str) -> list[list]:
    """
    :param str filename: path to file
    :returns list[list]: the adjacency matrix of a given graph
    """
    edges = []
    vershyny = set()

    with open(filename, 'r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            line = line.strip().replace(';', '').replace('->', '').split()
            if len(line) == 2:
                vertex, directional_point = line
                edges.append((vertex, directional_point))
                vershyny.update([vertex, directional_point])

    vershyny = sorted(vershyny)
    all_pairs = [[(i, j) for j in vershyny] for i in vershyny]

    matrix = [
        [1 if pair in edges else 0 for pair in row]
        for row in all_pairs
        ]

    return matrix


def read_adjacency_dict(filename: str) -> dict[int, list[int]]:
    """
    :param str filename: path to file
    :returns dict: the adjacency dict of a given graph
    """
    dictofgraph = {}
    with open(filename, 'r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            line = line.strip().replace(';', '').replace('->', '').split()
            if len(line) == 2:
                vertex, directional_point = map(int, line)
                if vertex not in dictofgraph:
                    dictofgraph[vertex] = []
                dictofgraph[vertex].append(directional_point)

    return dictofgraph


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
    visited = []  # список для збереження відвіданих вершин
    nodes_to_visit = [start]  #список в яких ми ще не були

    while nodes_to_visit:  # поки є вершини для відвідування
        vertex = nodes_to_visit.pop()  # беремо останню вершину зі списку
        if vertex not in visited:  # якщо вершина ще не була відвідана
            visited.append(vertex)  # додаємо вершину до списку відвіданих
            # додаємо суміжні вершини в зворотному порядку, щоб зберегти порядок обходу
            nodes_to_visit.extend(reversed(graph[vertex]))
    
#print(iterative_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0))


def iterative_adjacency_matrix_dfs(graph: list[list], start: int) ->list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> iterative_adjacency_matrix_dfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> iterative_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    visited = []  # список для збереження відвіданих вершин
    nodes_to_visit = [start]  # комірка з відвідуваннями, починається з стартової вершини

    while len(nodes_to_visit) > 0:  # поки є вершини для відвідування
        vertex = nodes_to_visit.pop()  # вибираємо останню вершину зі стека
        if vertex not in visited:  # якщо вершина ще не відвідана
            visited.append(vertex)  # додаємо її до списку відвіданих
            for neighbor in range(len(graph[vertex])): # додаємо суміжні вершини в стек в зворотньому порядку
                if graph[vertex][len(graph[vertex]) - 1 - neighbor] == 1:  # перевірка на зворотний порядок
                    if (len(graph[vertex]) - 1 - neighbor) not in visited:  # якщо сусід ще не відвіданий
                        nodes_to_visit.append(len(graph[vertex]) - 1 - neighbor)  # додаємо його в стек

    return visited
#print(iterative_adjacency_matrix_dfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0))



def recursive_adjacency_dict_dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    pass




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


def iterative_adjacency_matrix_bfs(graph: list[list[int]], start: int) ->list[int]:
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




def recursive_adjacency_matrix_bfs(graph: list[list[int]], start: int) ->list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> recursive_adjacency_matrix_bfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> recursive_adjacency_matrix_bfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    pass


def adjacency_matrix_radius(graph: list[list]) -> int:
    """
    :param list[list] graph: the adjacency matrix of a given graph
    :returns int: the radius of the graph
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    1
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0], [0, 1, 0]])
    2
    """
    pass


def adjacency_dict_radius(graph: dict[int: list[int]]) -> int:
    """
    :param dict graph: the adjacency list of a given graph
    :returns int: the radius of the graph
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    1
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [1]})
    2
    """
    pass


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
