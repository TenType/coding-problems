n, m = map(int, input().split())
f = []
checked = []
for i in range(0, n):
	f.append(list(map(int, input().split())))
	checked.append([])
	for j in range(0, m):
		checked[i].append(False)
print(f)
print(checked)

global streak
streak = 0
def findPools(x, y):
	if x < 0 or y < 0 or x > m-1 or y > n-1:
		return
	if checked[y][x]:
		return

	print(x, y)
	print(f)
	print(checked)
	checked[y][x] = True
	if f[y][x] == 1:
		streak += 1
	else:
		streak = 0
		print('Found at', x, y)

	findPools(x-1, y)
	findPools(x+1, y)
	findPools(x, y+1)
	findPools(x, y-1)

findPools(0, 0)
