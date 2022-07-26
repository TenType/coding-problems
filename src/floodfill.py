n, s1, s2 = map(int, input().split())
f = []
checked = []
temp = []
result = 0
for i in range(0, n):
	temp = list(map(int, input().split()))
	f.append([])
	checked.append([])
	for o in range(0, n):
		f[i].append(temp[o])
		checked[i].append(False)

# print(f)
# print(checked)

def flood(x, y):
	if x < 0 or y < 0 or x > n-1 or y > n-1:
		return
	if f[y][x] == 1 or checked[y][x]:
		return

	global result
	result += 1
	checked[y][x] = True
	# print(x, y)
	
	flood(x-1, y-1)
	flood(x+1, y+1)
	flood(x, y+1)
	flood(x, y-1)

flood(s1, s2)
print(result)
