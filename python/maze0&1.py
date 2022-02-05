n, m = map(int, input().split())
f = []
checked_def = []
temp = []
starting = []
for i in range(0, n):
	temp = list(map(int, input().split()))
	f.append([])
	checked_def.append([])
	for o in range(0, n):
		f[i].append(temp[o])
		checked_def[i].append(False)

# print(f)
# print(checked)

def maze(x, y, cell, checked):
	if x < 0 or y < 0 or x > n-1 or y > n-1:
		return
	if f[y][x] == cell or checked[y][x]:
		return

	print(x, y)
	global result
	result += 1
	checked[y][x] = True

##    cell = f[y][x]
##    if cell == 0:
##        cell = 1
##    else:
##        cell = 0
		
	# print(x, y)
	
	maze(x-1, y, f[y][x], checked)
	maze(x+1, y, f[y][x], checked)
	maze(x, y+1, f[y][x], checked)
	maze(x, y-1, f[y][x], checked)

for i in range(0, m):
	s1, s2 = map(int, input().split())
	result = 0
	maze(s1-1, s2-1, 'null', checked_def)
	print(result)
