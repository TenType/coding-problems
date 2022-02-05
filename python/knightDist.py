x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

class Node:
	def __init__(self, x, y, dist=0):
		self.x = x
		self.y = y
		self.dist = dist

def isInside(x, y):
	if (x >= 1 and x <= 20 and
		y >= 1 and y <= 20):
		return True
	return False
		

row = [2, 2, -2, -2, 1, 1, -1, -1, 2, 2, -2, -2]
col = [-1, 1, 1, -1, 2, -2, 2, -2, 2, -2, -2, 2]

def bfs(start, dest):
	visited = [[False for i in range(21)]
					  for j in range(21)]
	queue = [start]
	
	while len(queue) > 0:
		node = queue.pop(0)
		x = node.x
		y = node.y
		dist = node.dist

		if x == dest.x and y == dest.y:
			return dist

		visited[x][y] = True

		for i in range(0, 12):
			x_check = x + row[i]
			y_check = y + col[i]

			if not(visited[x_check][y_check]) and isInside(x_check, y_check):
				queue.append(Node(x_check, y_check, dist+1))

	return -1

print(bfs(Node(x1, y1), Node(1, 1)))
