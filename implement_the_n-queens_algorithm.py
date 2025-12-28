#!/usr/bin/env python3
def dfs_n_queens(n: int) -> list:
    """N-Queens Algorithm Implementation"""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 1:
        return []

    def queens_recur(n: int, i: int, a: list, b: list, c: list):
        # Adapted from "https://en.wikipedia.org/wiki/Eight_queens_puzzle"
        if i < n:
            for j in range(n):
                if j not in a and i + j not in b and i - j not in c:
                    yield from queens_recur(
                            n,
                            i + 1,
                            a + [j],
                            b + [i + j],
                            c + [i - j]
                    )
        else:
            yield a

    return list(queens_recur(n, 0, [], [], []))


def main():
    N = int(input("Enter number of Queens:\n"))
    for index, solution in enumerate(dfs_n_queens(N), start=1):
        print(index, solution)


if __name__ == '__main__':
    main()
