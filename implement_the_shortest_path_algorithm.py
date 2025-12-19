#!/usr/bin/env python3

INF = float('inf')


def shortest_path(matrix, start_node, target_node=None):
    n = len(matrix)
    if not isinstance(start_node, int):
        raise TypeError("start_node must be an integer")
    if start_node < 0 or start_node >= n:
        raise IndexError(
                "start_node must be >= 0 and < len(matrix)"
              )
    if target_node is not None:
        if not isinstance(target_node, int):
            raise TypeError("target_node must be an integer")
        if target_node < 0 or target_node >= n:
            raise IndexError(
                "target_node must be >= 0 and < len(matrix)"
              )
    distances = [INF] * n
    distances[start_node] = 0
    paths = [[node_no] for node_no in range(n)]
    visited = [False] * n

    for _ in range(n):
        min_distance = INF
        current = -1
        for node_no in range(n):
            if not visited[node_no] and distances[node_no] < min_distance:
                min_distance = distances[node_no]
                current = node_no

        if current == -1:
            break
        visited[current] = True

        for node_no in range(n):
            distance = matrix[current][node_no]
            if distance != INF and not visited[node_no]:
                new_distance = distances[current] + distance
                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance
                    paths[node_no] = paths[current] + [node_no]

    targets = [target_node] if target_node is not None else range(n)
    for node_no in targets:
        if node_no == start_node or distances[node_no] == INF:
            continue
        string_path = (str(n) for n in paths[node_no])
        path = ' -> '.join(string_path)
        print(
            f'\n{start_node}-{node_no} distance: {distances[node_no]}'
            f'\nPath: {path}'
        )

    return distances, paths


def main():
    adj_matrix = [
        [0, 5, 3, INF, 11, INF],
        [5, 0, 1, INF, INF, 2],
        [3, 1, 0, 1, 5, INF],
        [INF, INF, 1, 0, 9, 3],
        [11, INF, 5, 9, 0, INF],
        [INF, 2, INF, 3, INF, 0],
    ]

    adj_matrix_2 = [
        [0, 6, INF, 1, INF],
        [6, 0, 5, 2, 2],
        [INF, 5, 0, INF, 5],
        [1, 2, INF, 0, 1],
        [INF, 2, 5, 1, 0]
    ]

    # shortest_path(adj_matrix, 0, 5)
    try:
        print(shortest_path(adj_matrix_2, 0, 1))
    except TypeError as e:
        print(f"TypeError: {e}")
    except IndexError as e:
        print(f"IndexError: {e}")


if __name__ == '__main__':
    main()
