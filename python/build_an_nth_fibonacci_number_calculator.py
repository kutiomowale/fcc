#!/usr/bin/env python3
"""Build an Nth Fibonacci Number Calculator
   Using a dynamic programming approach
   """


def fibonacci(n):
    """Build an Nth Fibonacci Number Calculator
    Using a dynamic programming approach
    """
    if not isinstance(n, int):
        raise TypeError("n must be a positive integer")
    if n < 0:
        raise ValueError("n cannot be less than zero")
    sequence = [0, 1]
    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[n]


def main():
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(5))
    print(fibonacci(10))
    print(fibonacci(15))


if __name__ == '__main__':
    main()
