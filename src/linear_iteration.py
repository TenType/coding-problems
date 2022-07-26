n = int(input())
f = [1]
for i in range(1, n+1):
	if i <= 1:
		f.append(1)
	else:
		f.append((3 * f[1] + 2 * f[0]) % 1000000007)
		f.pop(0)
print(f[-1] % 1000000007)

##import sys
##sys.setrecursionlimit(20000)
##from functools import lru_cache
##
##n = int(input())
##
##@lru_cache(maxsize=None)
##def iterate(n):
##    if n <= 1:
##        return 1
##    else:
##        return (3 * iterate(n - 1) + 2 * iterate(n - 2)) % 1000000007
##print(iterate(n))
