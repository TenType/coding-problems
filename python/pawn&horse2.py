n, m, x, y = map(int, input().split())
horse_position = [[x,y],[x-1,y-2], [x-1, y+2], [x+1, y-2], [x+1, y+2], [x-2, y-1], [x-2, y+1], [x+2, y-1], [x+2, y+1]]
#print(horse_position)

f = [[0, 1]]

#calculating ways without hourse
for i in range(1, n+1):
	f.append([1])
	if ([i, 0] in horse_position):
		f[i][0] = 0
	#print("i = {}".format(i))
	#print(f)
	for j in range(1, m+1):
		if (i == 1):
			f[0].append(1) # add 1 to f[0][j]
			if ([0, j] in horse_position):
				f[0][j] = 0
		f[i].append(f[i-1][j] + f[i][j-1]) # f(n,m) = f(n, m-1) + f(n-1, m)
		#print("i = {}; j ={}" .format(i, j))
		if ([i,j] in horse_position):
			f[i][j] = 0
		#print(f)


print(f[n][m])
