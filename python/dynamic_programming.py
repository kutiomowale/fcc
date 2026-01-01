#!/usr/bin/env python3
counter = [0]


def climb_stairs(n):
    counter[0] += 1
    if n <= 2:
        return n
    return climb_stairs(n - 1) + climb_stairs(n - 2)


def climb_stairs_mem(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return n
    memo[n] = climb_stairs_mem(n-1, memo) + climb_stairs_mem(n-2, memo)
    return memo[n]


def climb_stairs_tb(n):
    if n < 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        counter[0] += 1
    return dp[n]


def climb_stairs_opt(n):
    if n < 2:
        return n
    prev2, prev1 = 1, 2
    for i in range(3, n + 1):
        current = prev1 + prev2
        counter[0] += 1
        prev2, prev1 = prev1, current
    return prev1


def min_coins(amount, coins):
    """Find minimum amount of coins needed to make the given amount"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                counter[0] += 1
    return dp[amount] if dp[amount] != float('inf') else -1


def main():
    print(climb_stairs(30))
    print(f"{counter[0]} function calls")

    counter[0] = 0
    print(climb_stairs_mem(30))
    print(f"{counter[0]} function calls")

    counter[0] = 0
    print(climb_stairs_tb(30))
    print(f"{counter[0]} calculations")

    counter[0] = 0
    print(climb_stairs_opt(30))
    print(f"{counter[0]} calculations")

    counter[0] = 0
    print(min_coins(3, [2]))
    print(f"{counter[0]} calculations")


if __name__ == '__main__':
    main()
