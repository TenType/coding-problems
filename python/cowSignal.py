m, n, k = map(int, input().split())
f = []
for i in range(0, m):
	f.append(list(str(input())))

for j in range(0, m):
	for t in range(0, k):
		result = ''
		for o in range(0, n):
			for p in range(0, k):
				result = str(result) + str(f[j][o])
		print(result)
