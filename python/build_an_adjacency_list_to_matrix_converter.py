#!/usr/bin/env python3
def adjacency_list_to_matrix(adj_list):
    """Convets an adjacency list to an adjacency matrix
    @adj_list is a dictionary whose keys are integers representing a node,
    and values are lists of nodes
    """
    if not isinstance(adj_list, dict):
        raise TypeError("Must be a dictionary")
    n = len(adj_list)
    for key in adj_list:
        if not isinstance(key, int):
            raise TypeError("Each key must be an integer")
        if key < 0 or key >= n:
            raise ValueError(
                    "keys must be >= 0 and be less than"
                    " the length of the adjacency list"
                  )
    for value in adj_list.values():
        if not isinstance(value, list):
            raise TypeError("Dictionary values must be lists")
        for num in value:
            if not isinstance(num, int):
                raise TypeError("List elementss must be integers")
            if num < 0 or num >= n:
                raise ValueError(
                        "Entry must be >= 0 and less than the length"
                        " of the adjacency list"
                      )
            if value.count(num) != 1:
                raise ValueError("Entries must be unique")

    adj_matrix = [
              [1 if j in adj_list[i] else 0 for j in range(n)]
              for i in range(n)
            ]
    for row in adj_matrix:
        print(row)
    return adj_matrix


def main():
    my_adj_list = {
     0: [1, 2],
     1: [2],
     2: [0, 3],
     3: [2]
    }
    print(adjacency_list_to_matrix(my_adj_list))


if __name__ == '__main__':
    main()
