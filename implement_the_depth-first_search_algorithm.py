#!/usr/bin/env python3
def dfs(adj_matrix, start_node):
    """
    >>> print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))
    [1, 0, 2, 3]
    >>> print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3))
    [3, 2, 1, 0]
    >>> print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3))
    [3]
    >>> print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3))
    [3, 2]
    >>> print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0))
    [0, 1]
    """
    if not isinstance(start_node, int):
        raise TypeError("Node label must be an integer")
    if start_node < 0:
        raise ValueError("Start node cannot be less than 0")
    n = len(adj_matrix)
    if start_node >= n:
        raise ValueError(
                "Start node must between 0 and n - 1, n being"
                "length of the matrix"
              )
    visited = [False] * n
    result = []

    def dfs_visit(node):
        visited[node] = True
        result.append(node)
        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs_visit(neighbor)

    dfs_visit(start_node)
    return result
#


def main():
    pass


if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()
