n, m, t = map(int, input().split())
sX, sY, fX, fY = map(int, input().split())
f = []
checked_def = []
result = 0

for i in range(0, n):
	f.append([])
	checked_def.append([])
	for j in range(0, n):
		f[i].append(0)
		checked_def[i].append(False)

for i in range(0, t):
	tX, tY = map(int, input().split())
	f[tY-1][tX-1] = 1

# print(f)
# print(checked_def)

def maze(x, y, checked):
	# print(x, y, checked)
	if x < 0 or y < 0 or x > n-1 or y > n-1:
		return
	if f[y][x] == 1 or checked[y][x]:
		return

	if x == fX-1 and y == fY-1:
		global result
		result += 1
		return

	checked[y][x] = True
	# print(x, y)
	
	maze(x-1, y, checked)
	maze(x+1, y, checked)
	maze(x, y+1, checked)
	maze(x, y-1, checked)

maze(sX-1, sY-1, checked_def)
print(result)
