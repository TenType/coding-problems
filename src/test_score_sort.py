n = int(input())
scores = []
for i in range(0, n):
	scores.append(list(map(str, input().split())))
	scores[i][1] = int(scores[i][1])
	scores[i][2] = int(scores[i][2])
	scores[i].append(i)
	scores[i].append(scores[i][1] + scores[i][2])

def sort(f):
	for z in range(1, len(f)):
		q = 1
		while q != len(f):
			if f[q-1][4] < f[q][4]:
				temp = f[q]
				f[q] = f[q-1]
				f[q-1] = temp
			elif f[q-1][4] == f[q][4]:
				if f[q-1][3] > f[q][3]:
					temp = f[q]
					f[q] = f[q-1]
					f[q-1] = temp
				
			q += int(1)

	return f


result = sort(scores)


for i in range(0, len(result)):
	print(result[i][0], result[i][1], result[i][2], result[i][4])
