import sys
from functools import lru_cache

sys.setrecursionlimit(5000)
n = int(input())

@lru_cache(maxsize=None)
def factorial(n):
	if n <= 0:
		return 1

	return(n * factorial(n-1) % 998244353)

print(factorial(n) % 998244353)
