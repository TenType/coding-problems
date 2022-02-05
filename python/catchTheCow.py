import sys
sys.setrecursionlimit(20000)
from functools import lru_cache

n, k = map(int, input().split())

visited = []
queue = [n]
steps = [0]

@lru_cache(maxsize=None)
def bfs():
	while len(queue) > 0:
		if queue[0] not in visited:
			if search(queue[0]):
				break
		
		queue.pop(0)
		steps.pop(0)

		# print(queue)
		# print(steps)
	print(steps[0])

@lru_cache(maxsize=None)
def search(x):
	visited.append(x)
	if x == k:
		return True
			
	queue.append(x+1)
	queue.append(x-1)
	queue.append(x*2)

	for i in range(0, 3):
		steps.append(steps[0]+1)
		
	return False
	  
bfs()
