n, t = map(int, input().split())
f = []
results = [-1, -1, -1, -1]
for i in range(0, n):
	f.append(list(map(int, input().split())))
# print(f)

for j in range(0, n):
	if t in range(f[j][4], f[j][5]):
		for k in range(0, 4):
			if f[j][k] > results[k]:
				results[k] = f[j][k]

for m in range(0, 4):
	print(results[m])
