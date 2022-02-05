n, m = map(int, input().split())
f = []
checked_def = []
treasures_def = 0
result = []

for i in range(0, n):
	f.append([char for char in str(input())])
	checked_def.append([])
	for j in range(0, m):
		checked_def[i].append(False)

print(f)
print(checked_def)

def maze(x, y, checked, treasures):
	# print(x, y, checked)
	if x < 0 or y < 0 or x > m-1 or y > n-1:
		# print('Out of bounds', x, y)
		return
	if f[y][x] == '#' or checked[y][x]:
		# print('Visited/obstacle', x, y)
		return

	print(x, y)
	if x == m-1 and y == n-1:
		global result
		print('Completed with', treasures)
		result.append(treasures)
		return

	checked[y][x] = True

	if f[y][x] != '*':
		treasures += int(f[y][x])
		print('Treasure found at', x, y, int(f[y][x]))
	
	
	maze(x-1, y, checked, treasures)
	maze(x+1, y, checked, treasures)
	# print('=== DOWN FOR', x, y, '===')
	maze(x, y+1, checked, treasures)
	maze(x, y-1, checked, treasures)

maze(0, 0, checked_def, treasures_def)
print(result)
