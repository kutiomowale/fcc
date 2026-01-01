#!/usr/bin/env python3
from build_an_adjacency_matrix_to_list_converter import adj_matrix_to_list


def dfs_adj_list_stack(adj_list, start_node):
    stack = [start_node]
    order = []
    n = len(adj_list)
    visited = [False] * n
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            order.append(node)
            for i in range(len(adj_list[node]) - 1, -1, -1):
                if not visited[adj_list[node][i]]:
                    stack.append(adj_list[node][i])

    return order


def dfs_adj_list_recursion(adj_list, start_node):
    n = len(adj_list)
    visited = [False] * n
    order = []

    def dfs_adj_list_recursion_visit(node):
        if not visited[node]:
            visited[node] = True
            order.append(node)
            for neighbor in adj_list[node]:
                dfs_adj_list_recursion_visit(neighbor)

    dfs_adj_list_recursion_visit(start_node)
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
    print("\nDepth First Search of the list using a stack")
    print(dfs_adj_list_stack(adj_list, 0))
    print("\nDepth First Search of the list using recursion")
    print(dfs_adj_list_recursion(adj_list, 0))


if __name__ == '__main__':
    main()
