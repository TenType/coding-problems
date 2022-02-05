from functools import lru_cache
import sys
sys.setrecursionlimit(20000)

n = int(input())
f = []
global combos
combos = 0

for z in range(1, n+1):
	a, b = map(str, input().split())
	f.append(int(b))

# @lru_cache(maxsize=None)
def swap(x, l, r):
	y = list(x)
	temp = y[l]
	y[l] = y[r]
	y[r] = temp
	x = tuple(y)
	# print(x)

# @lru_cache(maxsize=None)
def permutate(x, l):
	
	if l == len(x) - 1:
		# check if descending
		# print(x)

		for m in range(0, len(x) - 1):
			if x[m] > x[m-1]:
				return

		global combos
		combos += 1
		return

	
	for i in range(l, len(x)):
		swap(x, l, i)
		
		permutate(x, l+1)

		swap(x, l, i)

permutate(tuple(f), 0)
print(combos % 1000000007)
