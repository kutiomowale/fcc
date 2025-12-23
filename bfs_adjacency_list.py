#!/usr/bin/env python3
from build_an_adjacency_matrix_to_list_converter import adj_matrix_to_list


def bfs_adjacency_list(adj_list, start_node):
    from collections import deque
    n = len(adj_list)
    visited = [False] * n
    queue = deque([start_node])
    order = ""
    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            order += f" -> {node}"
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)

    return order

def main():
    adj_matrix = [
            [0, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1, 1],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
    ]

    print("Adjacency Matrix")
    for node in adj_matrix:
        print(node)

    print("\nConverted to an Adjacency list")
    adj_list = adj_matrix_to_list(adj_matrix)
    print("\nBreadth First Search of the list using a Queue")
    print(bfs_adjacency_list(adj_list, 0))


if __name__ == '__main__':
    main()
