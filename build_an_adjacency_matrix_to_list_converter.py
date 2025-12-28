#!/usr/bin/env python3
"""
Program to convert an adjacency matrix to an adjacency list.
The graphs are unweighted graphs.
Usage Examples:
>>> validate_adj_matrix([[0, 1], [1, 0]])
>>> validate_adj_matrix([[0, '1'], [1, 0]])    # string instead of an integer
Traceback (most recent call last):
    ...
TypeError: Inner lists must contain only integers
"""


def validate_adj_matrix(adj_matrix):
    """If the adjacency matrix @adj_matrix  is valid, no error is raised.

    The adjacency matrix is valid when:
    It is a list of lists,
    Each inner list has the same length as the adjacency matrix itself,
    Each inner list must be made of integers,
    The integers can only be 0 or 1,
    There must be at least one 0 in each inner list.

    Otherwise, a relevant error is raised
    >>> validate_adj_matrix(5)
    Traceback (most recent call last):
        ...
    TypeError: adj_matrix must be a list
    >>> validate_adj_matrix([3])
    Traceback (most recent call last):
       ...
    TypeError: adj_matrix must be a list of lists of integers
    >>> validate_adj_matrix([[0, 1]])
    Traceback (most recent call last):
        ...
    ValueError: Each list of integers should have the same length as the adjacency matrix
    >>> validate_adj_matrix([['0']])
    Traceback (most recent call last):
        ...
    TypeError: Inner lists must contain only integers
    >>> validate_adj_matrix([[5]])
    Traceback (most recent call last):
        ...
    ValueError: Only the integers 0 and 1 allowed
    >>> validate_adj_matrix([[1]])
    Traceback (most recent call last):
        ...
    ValueError: Inner lists must have at least one 0
    >>> validate_adj_matrix([[0]])
    """
    if not isinstance(adj_matrix, list):
        raise TypeError("adj_matrix must be a list")
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
                raise TypeError("Inner lists must contain only integers")
            if node != 0 and node != 1:
                raise ValueError("Only the integers 0 and 1 allowed")
        if 0 not in element:
            raise ValueError("Inner lists must have at least one 0")


def adj_matrix_to_list(adj_matrix):
    """Converts an adjacency matrix to a list
    Prints and return the result
    """
    validate_adj_matrix(adj_matrix)
    n = len(adj_matrix)
    adj_list = [[] for _ in range(n)]
    for node in range(n):
        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1:
                adj_list[node].append(neighbor)
    for node in adj_list:
        print(node)
    return adj_list


def main():
    adj_matrix_to_list(
            [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
    )
    adj_matrix_to_list(
            [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
    )
    adj_matrix_to_list(
            [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
    )
    adj_matrix_to_list(
            [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
    )
    adj_matrix_to_list(
            [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
    )


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
