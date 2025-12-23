#!/usr/bin/env python3
"""Implementation of a Breadth First Search Algorithm,
For an unweighted graph.
The Graph is implemented as an adjacency matrix
"""


def validate_adj_matrix_and_start_node(adj_matrix, start_node):
    """If @adj_matrix and @start_node is valid, no error is raised.
    The start node is valid when it is an integer,
    greater than or equal to zero and,
    less than the length of the adjacency matrix.

    The adjacency matrix is valid when:
    It is a list of lists,
    Each inner list has the same length as the adjacency matrix itself,
    Each inner list must be made of integers,
    The integers can only be 0 or 1,
    There must be at least one 0 in each inner list.

    Otherwise, a relevant error is raised
    """
    if not isinstance(adj_matrix, list):
        raise TypeError(
                f"adj_matrix must be a list not a: {type(adj_matrix)}"
               )
    n = len(adj_matrix)
    for element in adj_matrix:
        if not isinstance(element, list):
            raise TypeError("adj_matrix must be a list of lists of integers")
        if len(element) != n:
            raise ValueError(
                    "Each list of integers should have the same "
                    "length as the adjacency matrix"
                  )
        for node in element:
            if not isinstance(node, int):
                raise TypeError(
                        f"Inner lists must contain integers not: {type(node)}"
                      )
            if node != 0 and node != 1:
                raise ValueError("Only the integers 0 and 1 allowed")
        if 0 not in element:
            raise ValueError("Inner lists must have at least one 0")

    if not isinstance(start_node, int):
        raise TypeError("start_node must be an integer")
    if start_node < 0 or start_node >= n:
        raise ValueError(
                "start node must be >= 0 and < length of the "
                "adjacency matrix"
              )


def bfs(adj_matrix, start_node):
    """Breadth first search on @adj_matrix
    starting from @start_node
    >>> bfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1)
    [1, 0, 2, 3]
    >>> bfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3)
    [3, 2, 1, 0]
    >>> bfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3)
    [3]
    >>> bfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3)
    [3, 2]
    >>> bfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0)
    [0, 1]
    """
    validate_adj_matrix_and_start_node(adj_matrix, start_node)
    n = len(adj_matrix)
    from collections import deque
    queue = deque([start_node])
    order = []
    visited = [False] * n
    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            order.append(node)
            for neighbor in range(n):
                if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                    queue.append(neighbor)

    return order


def main():
    my_adj_matrix = [
            [0, 1, 0, 1, 0],
            [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0]
    ]
    print(bfs(my_adj_matrix, 0))


if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()
