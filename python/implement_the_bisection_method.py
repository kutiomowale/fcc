#!/usr/bin/env python3
def square_root_bisection(number, tolerance=1e-7, max_iter=100):
    if number < 0:
        raise ValueError(
                "Square root of negative number is not "
                "defined in real numbers"
        )
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    if number < 1:
        high = 1
    else:
        high = number
    low = 0
    mid = (low + high) / 2
    counter = 0
    while counter <= max_iter:
        mid = (low + high) / 2
        if abs(mid**2 - number) <= tolerance:
            break
        elif mid**2 > number:
            high = mid
        else:
            low = mid
        counter += 1
    else:
        print(
            f"Failed to converge within {max_iter}"
            f" iterations"
        )
        return None
    print(f"The square root of {number} is approximately {mid}")
    return mid
