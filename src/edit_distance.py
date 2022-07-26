def editDistance(word1, word2):
	x = len(word1)
	y = len(word2)
	table = [[0] * (y+1) for _ in range(x+1)]
	# print(table)

	for i in range(x+1):
		table[i][0] = i
	for j in range(y+1):
		table[0][j] = j

	# print(table)

	for i in range(1, x+1):
		for j in range(1, y+1):
			if word1[i-1] == word2[j-1]:
				table[i][j] = table[i-1][j-1]
			else:
				table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])
	# print(table)
	return table[-1][-1]

print(editDistance("hello", "world"))
