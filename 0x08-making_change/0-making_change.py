#!/usr/bin/python3
"""
determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Returns fewest number of coins needed to meet the total
    and returns -1 if the total cannot be met
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0
    remaining_total = total

    for coin in coins:
        if remaining_total == 0:
            break

        if coin <= remaining_total:
            coin_count += remaining_total // coin
            remaining_total = remaining_total % coin

    if remaining_total > 0:
        return -1

    return coin_count
