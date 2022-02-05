import sys
sys.setrecursionlimit(20000)
from functools import lru_cache

w, p = map(int, input().split())
a, b = map(int, input().split())

@lru_cache(maxsize=None)
def auction(i, n):
	if i > n:
		return 0
	if i == n:
		return 1

	return auction(i+a, w-p) + auction(i+b, w-p)

print(auction(0, w-p))

