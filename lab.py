"""
Lab 2. Mandryk Sophia and Pasternak Yuliia
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

    return visited


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

             # додаємо суміжні вершини в стек в зворотньому порядку >>>
            for neighbor in range(len(graph[vertex])):
                  # перевірка на зворотний порядок >>>
                if graph[vertex][len(graph[vertex]) - 1 - neighbor] == 1:
                      # якщо сусід ще не відвіданий >>
                    if (len(graph[vertex]) - 1 - neighbor) not in visited:
                          # додаємо його в стек >>>
                        nodes_to_visit.append(len(graph[vertex]) - 1 - neighbor)
    return visited


def recursive_adjacency_dict_dfs(graph: dict[int, list[int]], start: int,\
                                 visited=None) -> list[int]:
    """
    :param list[list] graph: the adjacency list of a given graph
    :param int start: start vertex of search
    :returns list[int]: the dfs traversal of the graph
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 0)
    [0, 1, 2]
    >>> recursive_adjacency_dict_dfs({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: []}, 0)
    [0, 1, 2, 3]
    """
    if visited is None: #робимо список вершин якщо його нема
        visited = []
    visited.append(start)#додаємо поточну вершину до списку відвіданих

    #для кожного сусіда поточної вершини перевіряємо, чи він ще не відвіданий >>>
    for neighbor in graph[start]:
        if neighbor not in visited:
            #викликаємо функцію для не відвіданого сусіда рекурсивно >>>
            recursive_adjacency_dict_dfs(graph, neighbor, visited)

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
    visited = []
    next_to_visit = [start] #робимо стек з початковою вершиною

    while next_to_visit: # ітеруємося поки черга не пуста
        vertex = next_to_visit.pop(0) #першу вершину з черги
        if vertex not in visited: #якщо вершинка ще не відвідана, додаємо її до списку відвіданих
            visited.append(vertex)
            for neighbour in graph[vertex]:
                # додаю до черги всіх сусідів, яких ще не відвідали і які не знаходяться в черзі >>>
                if neighbour not in visited and neighbour not in next_to_visit:
                    next_to_visit.append(neighbour)

    return visited


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
    visited = []
    next_to_visit = [start]

    while next_to_visit:
        vertex = next_to_visit.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            for i, connected in enumerate(graph[vertex]):
                #додаємо до черги всіх сусідів (індекси сусідів), які суміжні з поточною вершиною >>>
                if connected == 1 and i not in visited and i not in next_to_visit:
                    next_to_visit.append(i)

    return visited


def recursive_adjacency_matrix_bfs(graph: list[list[int]], start: int,\
                                   visited=None, next_to_visit=None) ->list[int]:
    """
    :param dict graph: the adjacency matrix of a given graph
    :param int start: start vertex of search
    :returns list[int]: the bfs traversal of the graph
    >>> recursive_adjacency_matrix_bfs([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0)
    [0, 1, 2]
    >>> recursive_adjacency_matrix_bfs([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]], 0)
    [0, 1, 2, 3]
    """
    if visited is None:
        visited = []
    if next_to_visit is None:
        next_to_visit = [start]
    if not next_to_visit:
        return visited
    vertex = next_to_visit.pop(0)
    if vertex not in visited:
        visited.append(vertex)
        neighbors = [i for i, is_connected in enumerate(graph[vertex])\
                     if is_connected == 1 and i not in visited]
        next_to_visit.extend(neighbors)

    return recursive_adjacency_matrix_bfs(graph, start, visited, next_to_visit)


def adjacency_matrix_radius(graph: list[list]) -> int:
    """
    :param list[list] graph: the adjacency matrix of a given graph
    :returns int: the radius of the graph
    >>> adjacency_matrix_radius([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    1
    """
    dictograph = {}

    for i in range(len(graph)):
        dictograph[i] = []
    for index1,el1 in enumerate(graph):
        for index2,_ in enumerate(el1):
            if el1[index2]:
                dictograph[index1].append(index2)

    # роблю список ексцентриситет, оскільки радіус - це наймешний з ексцентриситетів,
    # і я буду обирати зі списку >>>
    eccentricities = []

    for start in dictograph:
        # відстані до інших вершин >>>
        distances = {node: float('inf') for node in dictograph}
        distances[start] = 0
        # bfs
        queue = [start]

        while queue:
            current = queue.pop(0)
            for neighbour in dictograph[current]:
                if distances[neighbour] == float('inf'):
                    # якщо ще не відвідано вершинку >>>
                    distances[neighbour] = distances[current] + 1
                    queue.append(neighbour)
        eccentricities.append(max(distances.values()))

    return min(eccentricities)

def adjacency_dict_radius(graph: dict[int: list[int]]) -> int:
    """
    :param dict graph: the adjacency list of a given graph
    :returns int: the radius of the graph
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    1
    >>> adjacency_dict_radius({0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [1]})
    2
    """
    if not graph:
        return 0

    # роблю список ексцентриситет, оскільки радіус - це наймешний з ексцентриситетів,
    # і я буду обирати зі списку >>>
    eccentricities = []

    for start in graph:
        # відстані до інших вершин >>>
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        # bfs
        queue = [start]

        while queue:
            current = queue.pop(0)
            for neighbour in graph[current]:
                if distances[neighbour] == float('inf'):
                    # якщо ще не відвідано вершинку >>>
                    distances[neighbour] = distances[current] + 1
                    queue.append(neighbour)
        eccentricities.append(max(distances.values()))

    return min(eccentricities)




if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
