import sys
sys.setrecursionlimit(20000)
from functools import lru_cache
  
n, k = map(int, input().split())
  
@lru_cache(maxsize=None)
def steps(i, n):
	if i > n:
		return 0
	if i == n:
		return 1
 
	total = 0
	for x in range(1, k+1):
		total += steps(i+x, n)
 
	return total % 1000000007
	 
  
print(steps(0, n) % 1000000007)
