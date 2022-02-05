##n = int(input())
##k = int(input())
##x = 1
##for i in range(1, n-k):
## for e in range(n-k, n):
##   if (n-i-e) > 0:
##     x+=1
#print(x)

n, k = map(int, input().split())

if (k > n):
	print('0')
else:
	f = [[0, 0, 0], [0, 1, 0], [0, 1, 1]]

	if (n >= 3):
		for i in range(3, n+1):
			f.append([0])
			for j in range(1, i+1):
				if (i-j < j):
					f[i].append(f[i-1][j-1])
				else:
					f[i].append(f[i-1][j-1] + f[i-j][j])
	print(f[n][k])
