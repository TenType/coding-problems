##x = int(input())
##y = int(input())
##f = [[0, 1], [1]]
##
##for i in range(1, x):
##    f[0].append(1)
##for j in range(1, y):
##    f.append([1])
##for j in range(1, y+1):
##    for i in range(1, x+1):
##        print(f)
##        print(f[i-1][j])
##        print(f[i][j-1])
##        print("i = {}, j = {}".format(i, j))
##        f[i].append(f[i-1][j] + f[i][j-1])
##print(f)
##print(f[-1][-1])


n, m, x, y = map(int, input().split())
horse_x = [x, x+1, x+2, x-1, x-2, x+1, x+2, x-1, x-2]
horse_y = [y, y+2, y+1, y-2, y-1, y-2, y-1, y+2, y+1]
f = [[0, 1]]

def checkhorse(a, s):
	check = True
	for k in range(0, 9):
		if (a == horse_x[k] and s == horse_y[k]):
			check = False
			
	return check
	
for i in range(1, n+1):
	
	if checkhorse(i, 0):
		f.append([1])
	else:
		f.append([0])
		
	for j in range(1, m+1):
		if (i == 1):
			if checkhorse(i, j):
				f[0].append(1)
			else:
				f[0].append(0)
		
		if checkhorse(i, j):
			f[i].append(f[i-1][j] + f[i][j-1])
		else:
			f[i].append(0)
			
print(f[-1][-1])
