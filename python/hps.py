n = int(input())
cow1 = []
cow2 = []
combinations = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
results = []
for i in range(0, n):
	temp1, temp2 = map(int, input().split())
	cow1.append(temp1)
	cow2.append(temp2)
# print(cow1)
# print(cow2)

for j in range(0, 6):
	result = 0
	for k in range(0, n):
		index1 = combinations[j].index(cow1[k])
		index2 = combinations[j].index(cow2[k])

		# print(j, index1, index2)

		if (index1 == 0 and index2 == 1) or (index1 == 1 and index2 == 2) or (index1 == 2 and index2 == 0):
			result += 1
			# print(j, index1, index2, " Winner")
	results.append(result)
# print(results)
print(max(results))
