k, n = map(int, input().split())
f = []
pairs = []
for i in range(0, k):
	f.append(list(map(int, input().split())))
print(f)

for j in range(0, k): # iterate each line
	for l in range(0, n+1): # iterate each cow
		for m in range(0, l):
			print(j, l, m)
			if (j == 0):
				pairs.append([f[j][l], f[j][m]])
			elif any([f[j][l], f[j][m]] in b for b in pairs):
				pairs.pop(pairs.index([f[j][l], f[j][m]]))
	print(pairs)

print(pairs)
