#!/usr/bin/python3
"""
Minimum Operations script
"""


def minOperations(n):
    """
    Args:
        n: number of H characters to print
    Returns:
        (int): minimum number of operations needed to result
        in exactly n H characters
    """

    if not n or not isinstance(n, int) or n <= 1:
        return 0

    # get prime factors of n
    factors = primeFactorization(n)

    # sum prime factors
    return sum(factors)


def primeFactorization(n):
    """
    Args:
        n: number to factorize
    Returns:
        (list): prime factors of n
    """

    factors = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        else:
            divisor += 1

    return factors
