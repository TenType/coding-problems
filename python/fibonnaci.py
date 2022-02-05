n = int(input())
f = [0, 1, 1]
if n <= 0:
	print(0)
elif n <= 2:
	print(f[n])
else:
	for i in range(2, n+1):
		f.append(f[i-1] + f[i])
	print(f[-2])
