#!/usr/bin/python3
"""
calculates the fewest number of operations needed to result
in exactly n H characters in the file
"""


def minOperations(n):
    """
    return the minimum number (int) of operations needed to achieve the outcome
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
