import sys
sys.setrecursionlimit(20000)
from functools import lru_cache

# input
n, m = map(int, input().split())
trees = list(map(int, input().split()))
total = 0

# check highest tree
##check = 0
##for i in range(0, n):
##    if trees[i] > check:
##        check = trees[i]
check = max(trees)

# find output
@lru_cache(maxsize=None)
def woodchop(k):
	list2 = list(i-k if i>k else 0 for i in trees)
	total = sum(list2) 
	
	if total >= m:
		return k
		
	return woodchop(k-1)
	
	
##while total < m:
##    check -= 1
##    total = 0
##    for o in range(0, n):
##        if trees[o] > check:
##            total += trees[o] - check

print(woodchop(check))
