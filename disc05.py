#!/usr/bin/env python3
from operator import is_


def closest_number(nums, target):
    """Takes in a list of nums and returns the number that closest to the target."""
    return min(nums, key=lambda num: abs(num - target))


def max_product(s):
    """Non-consecutive"""
    s[1] = max(s[1], s[0])
    for i in range(2, len(s)):
        s[i] = max(max(s[i], s[i - 1]), s[i - 2] * s[i])
    return s[-1]

def max_cumulation(s):
    """Consecutive"""
    one_sum = 0
    max_sum = s[0]
    for i in range(len(s)):
        one_sum += s[i]
        max_sum = max(max_sum, one_sum)
        if one_sum < 0:
            one_sum = 0
    return max_sum

def max_addition(s):
    """Dynamic Partition(Consecutive)"""
    for i in range(1, len(s)):
        subMaxSum = max(s[i] + s[i - 1], s[i])
        s[i] = subMaxSum
    return max(s)

def filter_iter(iterable, f):
    filtered = filter(iterable, f)
    yield from filtered

def hailstone(n):
    if n == 1:
        yield 1
        yield from hailstone(n)
    elif n % 2 == 0:
        yield n
        n = n // 2
        yield from hailstone(n)
    else:
        yield n
        n = n * 3 + 1
        yield from hailstone(n)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order."""
    if n < 2:
        return
    if is_prime(n):
        yield n
    yield from primes_gen(n - 1)

if __name__ == "__main__":
    print(max_product([10, 9, 1, 3, 2]))
    print(max_addition([-2,1,-3,4,-1,2,1,-5,4]))
    hail_gen = hailstone(10)
    a = [next(hail_gen) for _ in range(10)]
    print(a)