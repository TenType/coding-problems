import sys
sys.setrecursionlimit(20000)
from functools import lru_cache


n = int(input())
f = []
startX = 0
startY = 0
visited = []
count = 0

@lru_cache(maxsize=None)
def split(word):
	return [char for char in word]

for i in range(0, n):
	text = split(str(input()))
	f.append(text)
	if '*' in text:
		startX = i
		startY = text.index('*')
		
	visited.append([])
	for o in range(0, len(f[i])):
		visited[i].append(False)

def labyrinth(x, y):
	if x < 0 or y < 0 or x > n-1 or y > n-1:
		return
	if f[y][x] == '-' or visited[y][x]:
		return

	global count
	count += 1
	visited[y][x] = True
	
	labyrinth(x-1, y)
	labyrinth(x+1, y)
	labyrinth(x, y+1)
	labyrinth(x, y-1)
	labyrinth(x-1, y+1)
	labyrinth(x-1, y-1)
	labyrinth(x+1, y+1)
	labyrinth(x+1, y-1)

labyrinth(startX, startY)
print(count)
