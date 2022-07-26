n = int(input())
f = []
temp = []
result = []
checked_default = []
for i in range(0, n):
	temp = list(map(int, input().split()))
	f.append([])
	checked_default.append([])
	for o in range(0, n):
		f[i].append(temp[o])
		checked_default[i].append(False)

def labyrinth(x, y, checked, steps):
	if x == n-1 and y == n-1:
		result.append(steps)
		return
	if x < 0 or y < 0 or x > n-1 or y > n-1:
		return
	if f[y][x] == 1 or checked[y][x]:
		return

	checked[y][x] = True
	# print(x, y)
	
	labyrinth(x-1, y, checked, steps+1)
	labyrinth(x+1, y, checked, steps+1)
	labyrinth(x, y+1, checked, steps+1)
	labyrinth(x, y-1, checked, steps+1)

labyrinth(0, 0, checked_default, 1)
print(result.count(min(result)))
print(min(result))
