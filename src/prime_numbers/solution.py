from math import sqrt

def solution(n: int) -> list[int]:
    primes = [True] * n
    primes[0] = False
    primes[1] = False

    for i in range(2, int(sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False

    return [index for index, check in enumerate(primes) if check]
